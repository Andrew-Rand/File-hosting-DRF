import os
import shutil
from datetime import datetime, timedelta
from typing import Dict, Any

from PIL import Image

from src.accounts.models import User
from src.basecore import logger_conf
from src.etl import celery_app
from src.fileservice.constants import LARGE_FILE_LIMIT_SIZE, STD_TUMBS
from src.fileservice.filetype_constants import ALLOWED_FILETYPES
from src.fileservice.models import FileStorage, File
from src.fileservice.models.file_storage import TEMP_STORAGE
from src.fileservice.utils import is_all_chunk_uploaded, save_file, calculate_hash_md5, make_chunk_paths, \
    send_warning_email_to_user, make_chunk_dir_path, calculate_hash_md5_for_large_files

CHUNK_EXPIRATION_TIME = timedelta(days=7)
TUMBNAIL_SIZE = 250

logger = logger_conf.get_logger(__name__)


@celery_app.task
def task_build_file(user_id: str, temp_storage_id: str, permanent_storage_id: str, data: Dict[str, Any]) -> None:

    logger.info('Celery task for filebuild %s starts' % data.get('filename'))

    user = User.objects.get(id=user_id)
    permanent_storage = FileStorage.objects.get(id=permanent_storage_id)
    temp_storage = FileStorage.objects.get(id=temp_storage_id)

    chunks_dir_path = make_chunk_dir_path(temp_storage.destination, user_id, data)

    # check if the upload is complete
    chunk_paths = make_chunk_paths(chunks_dir_path, data)
    if not is_all_chunk_uploaded(chunk_paths):
        send_warning_email_to_user(
            user.email,
            f'The server cant build your file {data.get("filename")}, please try to upload again!'
        )

        logger.warning('File %s was not build, warning email send to user %s' % (data.get('filename'), user.email))
        raise FileExistsError

    # create final file from all chunks
    user_storage_path = os.path.join(permanent_storage.destination, str(user.id))
    os.makedirs(user_storage_path, 0o777, exist_ok=True)
    target_file_path = os.path.join(user_storage_path, data.get('filename'))
    save_file(target_file_path, chunk_paths)
    os.rmdir(chunks_dir_path)

    if int(data.get('total_size')) > LARGE_FILE_LIMIT_SIZE:
        file_hash = calculate_hash_md5_for_large_files(target_file_path)
    else:
        file_hash = calculate_hash_md5(target_file_path)
    if file_hash != data.get('file_hash'):
        send_warning_email_to_user(
            user.email,
            f'The server cant build your file {data.get("filename")}, please try to upload again!'
        )

        logger.warning('Hash of file %s incorrect, warning email send to user %s' % (data.get('filename'), user.email))
        raise FileExistsError

    relative_path = os.path.join(str(user.id), data.get('filename'))

    File.create_model_object(user, file_hash, permanent_storage, relative_path, data)

    logger.info('Celery task for filebuild %s сompleted successfully' % data.get('filename'))

    task_create_tumbnail.delay(permanent_storage.destination + '/' + relative_path, data.get('type'))


@celery_app.task
def task_delete_unbuilt_chunks() -> None:
    temp_storage = FileStorage.objects.get(type=TEMP_STORAGE)
    temp_storage_path = temp_storage.destination
    user_dirs = os.listdir(temp_storage_path)
    if user_dirs:
        for user_dir in user_dirs:
            dirpath_to_rm = os.path.join(temp_storage_path, user_dir)
            st = os.stat(dirpath_to_rm)
            mtime = st.st_mtime
            time_of_dir_mod = datetime.fromtimestamp(mtime)
            if datetime.utcnow() - time_of_dir_mod > CHUNK_EXPIRATION_TIME:
                shutil.rmtree(dirpath_to_rm, ignore_errors=True)


@celery_app.task
def task_clean_up_deleted_files() -> None:

    files_qs = File.all_objects.filter(is_alive=False)  # marked as deleted
    if not files_qs:
        logger.info('Deleted files not found')
        return
    for file in files_qs:
        file_path = file.absolute_path
        if not os.path.exists(file_path):
            logger.info('File %s not found' % file.name)
        else:
            os.remove(file_path)


@celery_app.task
def task_delete_file(file_id: str) -> None:

    try:
        file_obj = File.all_objects.get(id=file_id)
    except File.DoesNotExist:
        logger.info('File %s not found' % file_id)
        return
    file_path = file_obj.absolute_path
    if not os.path.isfile(file_path):
        logger.info('File %s not found' % file_obj.name)
        return
    os.remove(file_path)


@celery_app.task
def task_create_tumbnail(filepath: str, file_type: str) -> None:

    img_filetypes = [i for i in ALLOWED_FILETYPES if i[:5] == 'image']

    if file_type in img_filetypes:
        image = Image.open(filepath)
        tumbnail = image.resize((TUMBNAIL_SIZE, TUMBNAIL_SIZE))
    else:
        image = Image.open(STD_TUMBS.get(file_type))
        tumbnail = image.resize((TUMBNAIL_SIZE, TUMBNAIL_SIZE))

    tumbnail.save(f'{filepath.split(".")[0]}_tumbnail.png')
