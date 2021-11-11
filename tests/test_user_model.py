from typing import Tuple

import pytest

from src.accounts.models import User
from src.config.settings import INSTALLED_APPS, AUTH_USER_MODEL


class TestSettings:

    def test_account_is_configured(self) -> None:
        assert 'src.accounts' in INSTALLED_APPS
        assert 'accounts.User' == AUTH_USER_MODEL


class TestUserModel:

    @pytest.mark.django_db
    def test_user_create(self, create_user_and_get_token: Tuple[User, str]) -> None:
        assert User.objects.count() == 1

    @pytest.mark.django_db
    def test_default_user_is_alive(self, create_user_and_get_token: Tuple[User, str]) -> None:
        user = create_user_and_get_token[0]
        assert user.is_alive

    @pytest.mark.django_db
    def test_default_user_is_active(self, create_user_and_get_token: Tuple[User, str]) -> None:
        user = create_user_and_get_token[0]
        assert user.is_active

    @pytest.mark.django_db
    def test_default_user_is_staff(self, create_user_and_get_token: Tuple[User, str]) -> None:
        user = create_user_and_get_token[0]
        assert not user.is_staff

    @pytest.mark.django_db
    def test_default_user_is_superuser(self, create_user_and_get_token: Tuple[User, str]) -> None:
        user = create_user_and_get_token[0]
        assert not user.is_superuser
