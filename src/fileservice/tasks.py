from celery import shared_task

from src.accounts.models import User
from src.config.celery import app
from src.fileservice.models import FileStorage
from src.fileservice.serializers.file_upload_parameters_serializer import FileUploadParametersSerializer
from src.fileservice.utils import build_file_from_chunks


@app.task
def task_build_file(user: User, temp_storage: FileStorage, permanent_storage: FileStorage, serializer: FileUploadParametersSerializer) -> None:
    build_file_from_chunks(user, temp_storage, permanent_storage, serializer)


@app.task
def test_task() -> str:
    return "Your celery task is working"
