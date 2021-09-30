from django.db import models

from src.basecore.base_model import BaseModel


class File(BaseModel):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='files', max_length=100, blank=True)

    def __unicode__(self):
        return self.title
