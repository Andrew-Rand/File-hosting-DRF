from typing import Tuple

import pytest

from src.accounts.models import User
from src.accounts.serializers.change_password_serializer import ChangePasswordSerializer
from src.accounts.serializers.user_login_serializer import UserLoginSerializer
from tests.constants import TEST_CHANGE_PASSWORD_SERIALIZER_DATA_VALID, TEST_PASSWORD


class TestChangePasswordSerializer:

    @pytest.mark.django_db
    def test_change_password_serializer_if_valid(self, create_user_and_get_token: Tuple[User, str]) -> None:

        serializer = ChangePasswordSerializer(data=TEST_CHANGE_PASSWORD_SERIALIZER_DATA_VALID,
                                              context={'user': create_user_and_get_token[0]})
        assert serializer.is_valid() is True

    @pytest.mark.django_db
    def test_change_password_serializer_if_incorrect_user(self) -> None:

        serializer = ChangePasswordSerializer(data=TEST_CHANGE_PASSWORD_SERIALIZER_DATA_VALID)
        assert serializer.is_valid() is False

    @pytest.mark.django_db
    def test_change_password_serializer_if_incorrect_password(self,
                                                              create_user_and_get_token: Tuple[User, str]
                                                              ) -> None:

        serializer = ChangePasswordSerializer(data={'password': '12345',
                                                    'new_password': '12345',
                                                    'new_password_repeated': '12345'
                                                    },
                                              context={'user': create_user_and_get_token[0]})
        assert serializer.is_valid() is False

    @pytest.mark.django_db
    def test_change_password_serializer_if_new_passwords_not_match(self,
                                                                   create_user_and_get_token: Tuple[User, str]
                                                                   ) -> None:

        serializer = ChangePasswordSerializer(data={'password': TEST_PASSWORD,
                                                    'new_password': '12345',
                                                    'new_password_repeated': '1234'
                                                    },
                                              context={'user': create_user_and_get_token[0]})
        assert serializer.is_valid() is False


class TestUserLoginSerializer:

    @pytest.mark.django_db
    def test_user_login_serializer_if_valid(self, create_user_and_get_token: Tuple[User, str]) -> None:

        serializer = UserLoginSerializer(data={'username': create_user_and_get_token[0].username,
                                               'password': TEST_PASSWORD})

        assert serializer.is_valid() is True

    @pytest.mark.django_db
    def test_user_login_serializer_if_user_does_not_exist(self) -> None:

        serializer = UserLoginSerializer(data={'username': '',
                                               'password': TEST_PASSWORD})

        assert serializer.is_valid() is False

    @pytest.mark.django_db
    def test_user_login_serializer_if_bad_password(self, create_user_and_get_token: Tuple[User, str]) -> None:

        serializer = UserLoginSerializer(data={'username': create_user_and_get_token[0].username,
                                               'password': ''})

        assert serializer.is_valid() is False
