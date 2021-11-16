from typing import Callable

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from src.fileservice.constants import FILE_BUILD_URL_NAME


class TestFileBuild:
    @pytest.mark.django_db
    def test_file_build_ok(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable,
            get_chunks: Callable
    ) -> None:

        user = get_user()
        url = reverse(FILE_BUILD_URL_NAME)
        url_query_params = get_chunks(user)
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.post(url + url_query_params)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_file_build_if_bad_query_params(
            self,
            test_client: APIClient,
            get_user: Callable,
            get_token: Callable
    ) -> None:

        user = get_user()
        url = reverse(FILE_BUILD_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.post(url)

        assert response.status_code == 400
