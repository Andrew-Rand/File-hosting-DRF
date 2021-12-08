from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User


class MyUserManager(BaseUserManager):
    def create_user(self, username: str = None, email: str = None, password: str = None, **extra_fields: Any) -> User:

        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.first_name = extra_fields.get('first_name', '')
        user.last_name = extra_fields.get('last_name', '')
        user.age = extra_fields.get('age', 50)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> User:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
