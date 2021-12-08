import uuid

from django.db import models

from src.basecore.managers import BaseModelManager


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_alive = models.BooleanField(default=True)

    objects = BaseModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using: bool = None, keep_parents: bool = False) -> None:
        self.is_alive = False
        self.save()
