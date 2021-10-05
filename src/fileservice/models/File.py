from django.db import models

from src.accounts.models import User
from src.basecore.base_model import BaseModel
from src.config import settings


class File(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files", null=True)
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='files', max_length=100, blank=True)

    def __unicode__(self):
        return self.title
