from django.db import models
from django.db.models import QuerySet


class BaseModelManager(models.manager):

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_alive=True)
