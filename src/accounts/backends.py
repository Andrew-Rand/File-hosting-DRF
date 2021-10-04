from typing import Any

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.request import Request


class EmailBackend(ModelBackend):

    def authenticate(self, request: Request, username: models.CharField = None, password: models.CharField = None, **kwargs: Any) -> object:
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            return None
        else:
            if user.password == password:
                return user
        return None
