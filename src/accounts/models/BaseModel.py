from django.db import models
import uuid


class BaseModel:
    id = models.CharField(default=uuid.uuid4)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
