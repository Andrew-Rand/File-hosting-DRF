import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings')
app = Celery('src.etl')
app.config_from_object('src.config.celery_config')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete_unbuilt_chunks': {
        'task': 'src.fileservice.tasks.delete_unbuilt_chunks',
        'schedule': crontab()
    }
}
