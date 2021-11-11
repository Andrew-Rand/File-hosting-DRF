from typing import Tuple

import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from src.accounts.models import User
from src.fileservice.constants import FILE_BUILD_URL_NAME


class TestFileBuild:
    @pytest.mark.django_db
    def test_file_build_ok(self, test_client: APIClient, chunks_create: str,
                           create_user_and_get_token: Tuple[User, str]) -> None:

        url = reverse(FILE_BUILD_URL_NAME)
        test_client.credentials(HTTP_Authorization=create_user_and_get_token[1])
        response = test_client.post(url + chunks_create)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_file_build_bad_queryset(self, test_client: APIClient, chunks_create: str,
                                     create_user_and_get_token: Tuple[User, str]) -> None:

        url = reverse(FILE_BUILD_URL_NAME)
        test_client.credentials(HTTP_Authorization=create_user_and_get_token[1])
        response = test_client.post(url)

        assert response.status_code == 400
