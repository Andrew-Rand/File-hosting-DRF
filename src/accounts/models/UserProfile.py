from django.contrib.auth.models import User
from django.db import models

from .BaseModel import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(verbose_name='name', max_length=30)
    about = models.TextField(verbose_name='About User', max_length=500)
