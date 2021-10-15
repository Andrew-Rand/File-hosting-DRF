from django.db import models

from src.basecore.base_model import BaseModel


STORAGE_TYPE_CHOICES = (
    ("TD", 'transitional_directory'),
    ("PD", 'permanent_directory'),
)


class FileStorage(BaseModel):
    type = models.CharField(max_length=30, choices=STORAGE_TYPE_CHOICES, default="TD")
    destination = models.CharField(max_length=256)
