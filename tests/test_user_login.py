from typing import Callable

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from src.accounts.constants import ACCOUNTS_LOGIN_URL_NAME


class TestUserLogin:

    @pytest.mark.django_db
    def test_login_view_ok(
            self,
            test_client: APIClient,
            get_user: Callable,
    ) -> None:

        user = get_user()
        url = reverse(ACCOUNTS_LOGIN_URL_NAME)
        data = {'username': user.username,
                'password': '1234Abc%%%'}

        response = test_client.post(url, data=data)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_login_view_if_bad_password(
            self,
            test_client: APIClient,
            get_user: Callable,
    ) -> None:

        user = get_user()
        url = reverse(ACCOUNTS_LOGIN_URL_NAME)
        data = {'username': user.username,
                'password': 'bad_password'}

        response = test_client.post(url, data=data)

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_login_view_if_bad_username(self, test_client: APIClient) -> None:

        url = reverse(ACCOUNTS_LOGIN_URL_NAME)
        data = {'username': 'user_who_does_not_exist',
                'password': '1234Abc%%%'}

        response = test_client.post(url, data=data)

        assert response.status_code == 400
