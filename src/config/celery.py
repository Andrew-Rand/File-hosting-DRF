import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings')
app = Celery('src.config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#  schedule for celery test task (every 5 seconds)
app.conf.beat_schedule = {
    'test-celery': {
        'task': 'src.fileservice.tasks.test_task',
        'schedule': 5.0
    }
}
