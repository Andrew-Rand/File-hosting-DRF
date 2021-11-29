from typing import Callable, Any

import pytest

from src.accounts.models import User
from src.config.settings import INSTALLED_APPS, AUTH_USER_MODEL


class TestSettings:

    def test_account_is_configured(self) -> None:
        assert 'src.accounts' in INSTALLED_APPS
        assert 'accounts.User' == AUTH_USER_MODEL


class TestUserModel:

    @pytest.mark.django_db
    def test_user_create(self, get_user: Callable[..., Any]) -> None:

        get_user()

        assert User.objects.count() == 1

    @pytest.mark.django_db
    def test_default_user_is_alive(self, get_user: Callable[..., Any]) -> None:

        user = get_user()

        assert user.is_alive

    @pytest.mark.django_db
    def test_default_user_is_active(self, get_user: Callable[..., Any]) -> None:

        user = get_user()

        assert user.is_active

    @pytest.mark.django_db
    def test_default_user_is_staff(self, get_user: Callable[..., Any]) -> None:

        user = get_user()

        assert not user.is_staff

    @pytest.mark.django_db
    def test_default_user_is_superuser(self, get_user: Callable[..., Any]) -> None:

        user = get_user()

        assert not user.is_superuser
