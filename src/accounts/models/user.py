from django.db import models

from src.accounts.managers import MyUserManager
from src.basecore.base_model import BaseModel
from ..validators import validate_age, validate_name, validate_password


class User(BaseModel):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    first_name = models.CharField(max_length=50, validators=[validate_name])
    last_name = models.CharField(max_length=50, validators=[validate_name])
    email = models.EmailField(unique=True, max_length=100)
    age = models.PositiveIntegerField(null=True, validators=[validate_age])
    password = models.CharField(max_length=100, validators=[validate_password])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)

    objects = MyUserManager()