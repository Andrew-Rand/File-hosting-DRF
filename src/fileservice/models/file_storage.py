from django.db import models

from src.basecore.base_model import BaseModel


TEMP_STORAGE = 'temp'
PERMANENT_STORAGE = 'permanent'

STORAGE_TYPE_CHOICES = (
    (TEMP_STORAGE, 'temp'),
    (PERMANENT_STORAGE, 'permanent'),
)


class FileStorage(BaseModel):
    type = models.CharField(max_length=128, choices=STORAGE_TYPE_CHOICES)
    destination = models.CharField(max_length=256)

    class Meta:
        db_table = "file_storages"
