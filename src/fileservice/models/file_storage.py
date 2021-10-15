from django.db import models

from src.basecore.base_model import BaseModel


STORAGE_TYPE_CHOICES = (
    (0, 'temp'),
    (1, 'permanent'),
)


class FileStorage(BaseModel):
    storage_type = models.PositiveSmallIntegerField(choices=STORAGE_TYPE_CHOICES, default=1)
    destination = models.FilePathField()
