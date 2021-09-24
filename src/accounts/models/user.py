from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from src.basecore.base_model import BaseModel


class User(AbstractBaseUser, BaseModel):
    username = None
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    email = models.EmailField(unique=True,
                              verbose_name='Email',
                              max_length=100)
    age = models.PositiveIntegerField(verbose_name='Age')
    password = models.CharField(verbose_name='Password', max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
