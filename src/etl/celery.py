import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings')
app = Celery('src.etl')
app.config_from_object('src.config.celery_config')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete_unbuilt_chunks': {
        'task': 'src.fileservice.tasks.task_delete_unbuilt_chunks',
        'schedule': crontab(minute=0, hour=0)  # everyday at midnight
    },
    'clean_up_deleted_files': {
        'task': 'src.fileservice.tasks.task_clean_up_deleted_files',
        'schedule': crontab(0, 0, day_of_month='5')  # 5th day every month
    }
}
