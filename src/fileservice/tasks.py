from typing import Any

from celery import shared_task
from rest_framework.request import Request

from src.accounts.models import User
import src.fileservice.views.file_build_view as file_build


@shared_task
def build_file(request: Request, *args: Any, user: User, **kwargs: Any) -> None:
    file_build.FileBuildView.post(request, *args, user, **kwargs)


@shared_task
def test_task() -> str:
    return "Your celery task is working"
