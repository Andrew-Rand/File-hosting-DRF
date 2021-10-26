from celery import shared_task


@shared_task
def build_file() -> str:
    return "Your celery task is working"
