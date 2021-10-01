from django.db import models

from src.basecore.base_model import BaseModel
from src.config import settings


class File(BaseModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files")
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='files', max_length=100, blank=True)

    def __unicode__(self):
        return self.title
