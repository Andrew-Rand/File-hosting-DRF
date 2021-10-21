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

    class Meta:
        db_table = 'files'

    def __repr__(self):
        return f'file {self.name} belongs to {self.user}'

    @staticmethod
    def create_model_object(user: User,
                            file_hash: str,
                            file_storage: FileStorage,
                            target_file_name: str,
                            validated_query_data: Dict[str, Any]) -> None:

        File.objects.create(user=user,
                            name=validated_query_data.get('filename'),
                            type=validated_query_data.get('type'),
                            storage=file_storage,
                            destination=target_file_name,
                            hash=file_hash,
                            size=validated_query_data.get('total_size'))
