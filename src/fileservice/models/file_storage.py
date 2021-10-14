from django.db import models

from src.accounts.models import User
from src.basecore.base_model import BaseModel

UPLOADING = 0
COMPLETE = 1

CHUNKED_UPLOAD_CHOICES = (
    (UPLOADING, 'Uploading'),
    (COMPLETE, 'Complete'),
)


class FileStorage(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files", null=True)
    filename = models.CharField(max_length=256)
    total_chunks = models.IntegerField()
    chunk_number = models.IntegerField()
    chunk_identifier = models.CharField()
    chunk_file = models.FileField(upload_to="home/tmp/uploads/chunks")
    status = models.PositiveSmallIntegerField(choices=CHUNKED_UPLOAD_CHOICES, default=UPLOADING)
