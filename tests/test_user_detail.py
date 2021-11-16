from typing import Callable

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from src.accounts.constants import ACCOUNTS_DETAIL_URL_NAME


class TestUserDetailGet:

    @pytest.mark.django_db
    def test_user_detail_get(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.get(url)

        assert response.status_code == 200
        assert response.data == {'id': str(user.id),
                                 'username': user.username,
                                 'first_name': user.first_name,
                                 'last_name': user.last_name,
                                 'email': user.email,
                                 'age': user.age}


class TestUserDetailPatch:

    TEST_NEW_USER_DATA = {
            'email': 'new@mail.ru',
            'age': 50,
            'first_name': 'new_name',
            'last_name': 'new_l_name'
        }

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_all_fields(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        data = self.TEST_NEW_USER_DATA
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result') == data
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_empty_data(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(user))
        response = test_client.patch(url, data={})
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result') == {}
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_email(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        test_field = 'email'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        data = {test_field: self.TEST_NEW_USER_DATA.get(test_field)}
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result').get(test_field) == data.get(test_field)
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_email_already_in_use(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        test_field = 'email'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        data = {test_field: 'test@mail.ru'}
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 400
        assert data_to_assert.get('result') is None
        assert data_to_assert.get('error_detail')[0] == {"email": ["user with this email already exists."]}

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_age(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        test_field = 'age'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        data = {test_field: self.TEST_NEW_USER_DATA.get(test_field)}
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result').get(test_field) == data.get(test_field)
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_first_name(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        test_field = 'first_name'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        data = {test_field: self.TEST_NEW_USER_DATA.get(test_field)}
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result').get(test_field) == data.get(test_field)
        assert data_to_assert.get('error_detail') is None

    @pytest.mark.django_db
    def test_user_detail_get_if_change_valid_last_name(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        test_field = 'last_name'

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        data = {test_field: self.TEST_NEW_USER_DATA.get(test_field)}
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.patch(url, data=data)
        data_to_assert = response.data.get('data')

        assert response.status_code == 200
        assert data_to_assert.get('result').get(test_field) == data.get(test_field)
        assert data_to_assert.get('error_detail') is None
