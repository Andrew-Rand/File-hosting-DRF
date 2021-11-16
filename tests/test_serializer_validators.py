from typing import Callable

import pytest

from src.accounts.serializers.change_password_serializer import ChangePasswordSerializer
from src.accounts.serializers.user_login_serializer import UserLoginSerializer


class TestChangePasswordSerializer:

    @pytest.mark.django_db
    def test_change_password_serializer_if_valid(self, get_user: Callable) -> None:

        user = get_user()

        serializer = ChangePasswordSerializer(
            data={
                'password': '1234Abc%%%',
                'new_password': '0Dc%0Dc%00',
                'new_password_repeated': '0Dc%0Dc%00',
            },
            context={'user': user})

        assert serializer.is_valid() is True

    @pytest.mark.django_db
    def test_change_password_serializer_if_incorrect_user(self) -> None:

        serializer = ChangePasswordSerializer(
            data={
                'password': '1234Abc%%%',
                'new_password': '0Dc%0Dc%00',
                'new_password_repeated': '0Dc%0Dc%00',
            })

        assert serializer.is_valid() is False

    @pytest.mark.django_db
    def test_change_password_serializer_if_incorrect_password(self, get_user: Callable) -> None:

        user = get_user()

        serializer = ChangePasswordSerializer(data={
                'password': '1234Abc%%1',
                'new_password': '1234Abc%%%',
                'new_password_repeated': '1234Abc%%%',
            },
            context={'user': user})

        assert serializer.is_valid() is False

    @pytest.mark.django_db
    def test_change_password_serializer_if_if_new_passwords_not_match(self, get_user: Callable) -> None:

        user = get_user()

        serializer = ChangePasswordSerializer(data={
                'password': '1234Abc%%%',
                'new_password': '0Dc%0Dc%00',
                'new_password_repeated': '0Dc%0Dc%01',
            },
            context={'user': user})

        assert serializer.is_valid() is False


class TestUserLoginSerializer:

    @pytest.mark.django_db
    def test_user_login_serializer_if_valid(self, get_user: Callable) -> None:

        user = get_user()

        serializer = UserLoginSerializer(data={'username': user.username,
                                               'password': '1234Abc%%%'})

        assert serializer.is_valid() is True

    @pytest.mark.django_db
    def test_user_login_serializer_if_user_does_not_exist(self) -> None:

        serializer = UserLoginSerializer(data={'username': '',
                                               'password': '1234Abc%%%'})

        assert serializer.is_valid() is False

    @pytest.mark.django_db
    def test_user_login_serializer_if_bad_password(self, get_user: Callable) -> None:

        user = get_user()

        serializer = UserLoginSerializer(data={'username': user.username,
                                               'password': ''})

        assert serializer.is_valid() is False
