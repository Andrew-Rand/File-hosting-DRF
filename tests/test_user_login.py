from typing import Tuple

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from src.accounts.constants import ACCOUNTS_LOGIN_URL_NAME
from src.accounts.models import User
from tests.constants import TEST_PASSWORD


class TestUserLogin:

    @pytest.mark.django_db
    def test_login_view_ok(self, test_client: APIClient,
                           create_user_and_get_token: Tuple[User, str]) -> None:

        url = reverse(ACCOUNTS_LOGIN_URL_NAME)
        data = {'username': create_user_and_get_token[0].username,
                'password': TEST_PASSWORD}
        response = test_client.post(url, data=data)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_login_view_if_bad_password(self, test_client: APIClient,
                                        create_user_and_get_token: Tuple[User, str]) -> None:

        url = reverse(ACCOUNTS_LOGIN_URL_NAME)
        data = {'username': create_user_and_get_token[0].username,
                'password': 'bad_password'}
        response = test_client.post(url, data=data)

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_login_view_if_bad_username(self, test_client: APIClient) -> None:

        url = reverse(ACCOUNTS_LOGIN_URL_NAME)
        data = {'username': 'user_who_does_not_exist',
                'password': TEST_PASSWORD}
        response = test_client.post(url, data=data)

        assert response.status_code == 400
