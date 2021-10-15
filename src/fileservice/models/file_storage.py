from django.db import models

from src.basecore.base_model import BaseModel


TEMP_DIR = 'temp'
PERMANENT_DIR = 'permanent'

STORAGE_TYPE_CHOICES = (
    ("tmp", 'temp_storage'),
    ("prm", 'permanent'),
)


class FileStorage(BaseModel):
    type = models.CharField(choices=STORAGE_TYPE_CHOICES, default="tmp")
    destination = models.CharField(max_length=256)
