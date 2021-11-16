import pytest
from django.urls import reverse

from rest_framework.test import APIClient

from src.accounts.constants import ACCOUNTS_REGISTER_URL_NAME


class TestUserRegister:

    @pytest.mark.django_db
    def test_register_view_ok(self, test_client: APIClient) -> None:

        url = reverse(ACCOUNTS_REGISTER_URL_NAME)
        data = {
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test_email@gmail.com',
            'password': '1234Abc%%%',
            'username': 'test_username'
        }

        response = test_client.post(url, data=data)

        assert response.status_code == 201

    @pytest.mark.django_db
    def test_register_view_bad(self, test_client: APIClient) -> None:

        url = reverse(ACCOUNTS_REGISTER_URL_NAME)

        response = test_client.post(url, data={})

        assert response.status_code == 400
