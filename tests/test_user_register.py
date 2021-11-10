import pytest
from django.urls import reverse

from rest_framework.test import APIClient

from src.accounts.constants import ACCOUNTS_REGISTER_URL_NAME
from tests.constants import TEST_USER_REGISTER_DATA


class TestUserRegister:

    @pytest.mark.django_db
    def test_register_view_ok(self, test_client: APIClient) -> None:
        url = reverse(ACCOUNTS_REGISTER_URL_NAME)
        data = TEST_USER_REGISTER_DATA
        response = test_client.post(url, data=data)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_register_view_bad(self, test_client: APIClient) -> None:
        url = reverse(ACCOUNTS_REGISTER_URL_NAME)
        data = {}
        response = test_client.post(url, data=data)
        assert response.status_code == 400
