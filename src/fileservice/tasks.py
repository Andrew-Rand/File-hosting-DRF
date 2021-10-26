from typing import Any

from celery import shared_task
from rest_framework.request import Request

from src.accounts.models import User
import src.fileservice.views.file_build_view as file_build
from src.fileservice.models import FileStorage
from src.fileservice.serializers.file_upload_parameters_serializer import FileUploadParametersSerializer
from src.fileservice.utils import build_file_from_chunks


@shared_task
def task_build_file(user: User, temp_storage: FileStorage, permanent_storage: FileStorage, serializer: FileUploadParametersSerializer) -> None:
    build_file_from_chunks(user, temp_storage, permanent_storage, serializer)


@shared_task
def test_task() -> str:
    return "Your celery task is working"
