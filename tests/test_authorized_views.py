from typing import Callable

import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from src.accounts.constants import ACCOUNTS_DETAIL_URL_NAME
from src.fileservice.constants import FILE_DETAIL_URL_NAME, FILE_DOWNLOAD_URL_NAME, FILE_UPLOAD_URL_NAME, \
    FILE_BUILD_URL_NAME, FILE_CHUNK_UPLOAD_URL_NAME, FILE_DOWNLOAD_ALL_URL_NAME, FILE_ALL_USER_FILES_URL_NAME
from tests.constants import TEST_QUERYSET_FOR_BUILD


class TestAuthorizedRequest:

    @pytest.mark.django_db
    def test_authorized_user_detail(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        url = reverse(ACCOUNTS_DETAIL_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(get_user()))

        response = test_client.get(url)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authorized_chunk_upload_get(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        url = reverse(FILE_CHUNK_UPLOAD_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(get_user()))

        response = test_client.get(url)

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_authorized_chunk_upload_post(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        url = reverse(FILE_CHUNK_UPLOAD_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(get_user()))

        response = test_client.get(url)

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_authorized_download_all_file_as_zip(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        url = reverse(FILE_DOWNLOAD_ALL_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(get_user()))

        response = test_client.get(url)

        assert response.status_code == 404

    @pytest.mark.django_db
    def test_authorized_all_user_files(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        url = reverse(FILE_ALL_USER_FILES_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(get_user()))

        response = test_client.get(url)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authorized_file_detail_get(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable,
            get_file: Callable
    ) -> None:

        user = get_user()
        file = get_file(user)
        url = reverse(FILE_DETAIL_URL_NAME, kwargs={'pk': str(file.id)})
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.get(url)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authorized_file_detail_patch(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable,
            get_file: Callable
    ) -> None:

        user = get_user()
        file = get_file(user)
        url = reverse(FILE_DETAIL_URL_NAME, kwargs={'pk': str(file.id)})
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.patch(url)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authorized_file_detail_delete(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable,
            get_file: Callable
    ) -> None:

        user = get_user()
        file = get_file(user)
        url = reverse(FILE_DETAIL_URL_NAME, kwargs={'pk': str(file.id)})
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.get(url)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authorized_file_download(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable,
            get_file: Callable
    ) -> None:

        user = get_user()
        file = get_file(user)
        url = reverse(FILE_DOWNLOAD_URL_NAME, kwargs={'pk': str(file.id)})
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.get(url)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authorized_file_upload(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        url = reverse(FILE_UPLOAD_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.post(url)

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_authorized_file_build(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        url = reverse(FILE_BUILD_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.post(url + TEST_QUERYSET_FOR_BUILD)

        assert response.status_code == 200
