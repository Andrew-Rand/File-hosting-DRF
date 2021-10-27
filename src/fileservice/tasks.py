from typing import Dict, Any

from src.etl import celery_app
from src.fileservice.utils import build_file_from_chunks


@celery_app.task
def task_build_file(user_id: str, temp_storage_id: str, permanent_storage_id: str, serializer: Dict[str, Any]) -> None:
    build_file_from_chunks(user_id, temp_storage_id, permanent_storage_id, serializer)


@celery_app.task
def test_task() -> str:
    return "Your celery task is working"
