from typing import Any

from celery import shared_task
from rest_framework.request import Request

from src.accounts.models import User
from src.fileservice.views.file_build_view import FileBuildView


@shared_task
def build_file(self, request: Request, *args: Any, user: User, **kwargs: Any) -> None:
    FileBuildView.post()

