from typing import Dict, Any

from django.db import models

from src.accounts.models import User
from src.basecore.base_model import BaseModel
from src.fileservice.models.file_storage import FileStorage


class File(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='files')
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=128)
    storage = models.ForeignKey(FileStorage, on_delete=models.DO_NOTHING, related_name='files')
    destination = models.CharField(max_length=256)
    hash = models.CharField(max_length=300)
    size = models.BigIntegerField()
    description = models.TextField(null=True)

    class Meta:
        db_table = 'files'

    def __repr__(self) -> str:
        return f'file {self.name} belongs to {self.user}'

    @staticmethod
    def create_model_object(user: User,
                            hash: str,
                            storage: FileStorage,
                            destination: str,
                            data: Dict[str, Any]) -> None:

        File.objects.create(user=user,
                            name=data.get('filename'),
                            type=data.get('type'),
                            storage=storage,
                            destination=destination,
                            hash=hash,
                            size=data.get('total_size'))

    @property
    def absolute_path(self) -> str:
        return self.storage.destination / self.destination
