from django.db import models

from src.accounts.models import User
from src.basecore.base_model import BaseModel
from src.fileservice.models.file_storage import FileStorage


class File(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="files")
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    destination = models.ForeignKey(FileStorage, on_delete=models.DO_NOTHING, related_name="files")
    hash = models.CharField(max_length=64)
    size = models.BigIntegerField()
