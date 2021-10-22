import os

from django.db import migrations

from src.config.settings import BASE_DIR
from src.fileservice.models.file_storage import TEMP_STORAGE, PERMANENT_STORAGE


def load_data(apps, shema_editor):

    storage_dir = os.path.join(BASE_DIR, 'storage')
    temp_dir = os.path.join(storage_dir, 'temp')
    permanent_dir = os.path.join(storage_dir, 'permanent')

    FileStorage = apps.get_model('fileservice', 'FileStorage')

    FileStorage(type=TEMP_STORAGE, destination=temp_dir).save()
    FileStorage(type=PERMANENT_STORAGE, destination=permanent_dir).save()


class Migration(migrations.Migration):
    dependencies = [
        ('fileservice', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
