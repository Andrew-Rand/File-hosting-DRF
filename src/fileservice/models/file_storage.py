from django.db import models

from src.basecore.base_model import BaseModel


STORAGE_TYPE_CHOICES = (
    ("trans", 'transitional'),
    ("perm", 'permanent'),
)


class FileStorage(BaseModel):
    type = models.CharField(choices=STORAGE_TYPE_CHOICES, default="trans")
    destination = models.CharField(max_length=256)
