from django.db import models

from src.accounts.models import User
from src.basecore.base_model import BaseModel


class File(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files", null=True)
    file_name = models.CharField(max_length=128)
    file_type = models.CharField(max_length=32)
    media_root = models.FilePathField()
    md5_hash = models.CharField()
    bytes_fields = models.CharField()
    dir_path = models.FilePathField()

    @property
    def get_file_name(self):
        return self.file_name
