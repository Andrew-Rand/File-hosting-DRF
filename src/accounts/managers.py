from typing import Any

from django.contrib.auth.base_user import BaseUserManager
# from src.accounts.models import User


class MyUserManager(BaseUserManager):
    def _create_user(self, username: str, email: str, password: str = None, **extra_fields: Any) -> Any:
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> Any:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
