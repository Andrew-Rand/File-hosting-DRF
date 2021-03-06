from typing import List

from django.db import models
from django.contrib.auth.hashers import check_password, make_password

from src.accounts.managers import MyUserManager
from src.basecore.base_model import BaseModel
from ..validators import validate_age, validate_name, validate_password


class User(BaseModel):

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS: List[str] = []

    username = models.CharField(max_length=50, validators=[validate_name], unique=True)
    first_name = models.CharField(max_length=50, validators=[validate_name])
    last_name = models.CharField(max_length=50, validators=[validate_name])
    email = models.EmailField(unique=True, max_length=100)
    age = models.PositiveIntegerField(null=True, validators=[validate_age])
    password = models.CharField(max_length=100, validators=[validate_password])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    def set_password(self, raw_password: str) -> None:
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password: str) -> bool:
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password: str) -> None:
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    @property
    def is_authenticated(self) -> bool:
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
