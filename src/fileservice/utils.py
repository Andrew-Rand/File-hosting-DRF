import hashlib
import os
from typing import List

from src.accounts.models import User
from src.basecore.custom_error_handler import BadRequestError
from src.fileservice.models import File, FileStorage
from src.fileservice.serializers.file_upload_parameters_serializer import FileUploadParametersSerializer


def calculate_hash_md5(file_path: str) -> str:
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def is_all_chunk_uploaded(chunk_paths) -> bool:
    upload_complete = all([os.path.exists(p) for p in chunk_paths])
    if upload_complete:
        return True
    else:
        return False


def get_chunk_name(uploaded_filename: str, chunk_number: int) -> str:
    return f'{uploaded_filename}_part_{chunk_number}'


def save_file(target_file_path: str, chunk_paths: List[str]) -> None:
    with open(target_file_path, 'ab') as target_file:
        for stored_chunk_file_name in chunk_paths:
            stored_chunk_file = open(stored_chunk_file_name, 'rb')
            target_file.write(stored_chunk_file.read())
            stored_chunk_file.close()
            os.unlink(stored_chunk_file_name)
    target_file.close()


def build_file_from_chunks(user: User, temp_storage: FileStorage, permanent_storage: FileStorage, serializer: FileUploadParametersSerializer) -> None:

    identifier = serializer.validated_data.get('identifier')
    filename = serializer.validated_data.get('filename')
    total_chunks = serializer.validated_data.get('total_chunk')

    # make temp directory
    user_dir_path = os.path.join(temp_storage.destination, str(user.id))
    chunks_dir_path = os.path.join(user_dir_path, identifier)

    # check if the upload is complete
    chunk_paths = [
        os.path.join(chunks_dir_path, get_chunk_name(filename, x))
        for x in range(1, total_chunks + 1)
    ]
    if not is_all_chunk_uploaded(chunk_paths):
        raise BadRequestError('There aren`t all chunks for this file. Try to continue upload chunks')

    # create final file from all chunks
    user_storage_path = os.path.join(permanent_storage.destination, str(user.id))
    os.makedirs(user_storage_path, 0o777, exist_ok=True)
    target_file_path = os.path.join(user_storage_path, filename)
    save_file(target_file_path, chunk_paths)
    os.rmdir(chunks_dir_path)

    file_hash = calculate_hash_md5(target_file_path)

    File.create_model_object(user, file_hash, permanent_storage, target_file_path, serializer.validated_data)
