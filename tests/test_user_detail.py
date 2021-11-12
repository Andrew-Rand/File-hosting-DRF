from typing import Tuple

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from src.accounts.constants import ACCOUNTS_DETAIL_URL_NAME
from src.accounts.models import User
from tests.constants import TEST_NEW_USER_DATA, TEST_EMAIL


class TestUserDetailGet:

    @pytest.mark.django_db
    def test_user_detail_get(self, test_client: APIClient,
                             create_user_and_get_token: Tuple[User, str]) -> None:
        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        user = create_user_and_get_token[0]
        token = create_user_and_get_token[1]
        test_client.credentials(HTTP_Authorization=token)
        response = test_client.get(url)

        assert response.status_code == 200
        assert response.data == {'id': str(user.id),
                                 'username': user.username,
                                 'first_name': user.first_name,
                                 'last_name': user.last_name,
                                 'email': user.email,
                                 'age': user.age}


class TestUserDetailPatch:

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_all_fields(self, test_client: APIClient,
                                                        create_user_and_get_token: Tuple[User, str]) -> None:

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        token = create_user_and_get_token[1]
        data = TEST_NEW_USER_DATA
        test_client.credentials(HTTP_Authorization=token)
        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result') == TEST_NEW_USER_DATA
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_empty_data(self, test_client: APIClient,
                                           create_user_and_get_token: Tuple[User, str]) -> None:

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        token = create_user_and_get_token[1]
        data = {}
        test_client.credentials(HTTP_Authorization=token)
        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result') == {}
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_email(self, test_client: APIClient,
                                                   create_user_and_get_token: Tuple[User, str]) -> None:

        test_field = 'email'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        token = create_user_and_get_token[1]
        data = {test_field: TEST_NEW_USER_DATA.get(test_field)}
        test_client.credentials(HTTP_Authorization=token)
        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result').get(test_field) == data.get(test_field)
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_email_already_in_use(self, test_client: APIClient,
                                                     create_user_and_get_token: Tuple[User, str]) -> None:

        test_field = 'email'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        token = create_user_and_get_token[1]
        data = {test_field: TEST_EMAIL}
        test_client.credentials(HTTP_Authorization=token)
        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 400
        assert data_to_assert.get('result') is None
        assert data_to_assert.get('error_detail')[0] == {"email": ["user with this email already exists."]}

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_age(self, test_client: APIClient,
                                                 create_user_and_get_token: Tuple[User, str]) -> None:

        test_field = 'age'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        token = create_user_and_get_token[1]
        data = {test_field: TEST_NEW_USER_DATA.get(test_field)}
        test_client.credentials(HTTP_Authorization=token)
        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result').get(test_field) == data.get(test_field)
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_first_name(self, test_client: APIClient,
                                                        create_user_and_get_token: Tuple[User, str]) -> None:

        test_field = 'first_name'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        token = create_user_and_get_token[1]
        data = {test_field: TEST_NEW_USER_DATA.get(test_field)}
        test_client.credentials(HTTP_Authorization=token)
        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result').get(test_field) == data.get(test_field)
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_last_name(self, test_client: APIClient,
                                                       create_user_and_get_token: Tuple[User, str]) -> None:

        test_field = 'last_name'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        token = create_user_and_get_token[1]
        data = {test_field: TEST_NEW_USER_DATA.get(test_field)}
        test_client.credentials(HTTP_Authorization=token)
        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result').get(test_field) == data.get(test_field)
        assert data_to_assert.get('error_detail') is None
