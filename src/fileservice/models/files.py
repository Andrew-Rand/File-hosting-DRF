from django.db import models

from src.accounts.models import User
from src.basecore.base_model import BaseModel


class File(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files", null=True)
    file = models.FileField(upload_to="home/tmp/uploads")
