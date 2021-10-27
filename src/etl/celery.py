import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings')
app = Celery('src.etl')
app.config_from_object('src.config.celery_config')
app.autodiscover_tasks()
