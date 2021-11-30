from typing import Callable, Any

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from src.fileservice.constants import FILE_BUILD_URL_NAME


class TestFileBuild:

    QUERY_PARAMS_ERROR_MESSAGE = {
        "resumableTotalChunks": [
            "This field is required."
        ],
        "resumableChunkNumber": [
            "This field is required."
        ],
        "resumableFilename": [
            "This field is required."
        ],
        "resumableIdentifier": [
            "This field is required."
        ],
        "resumableType": [
            "This field is required."
        ],
        "resumableTotalSize": [
            "This field is required."
        ],
        'resumableDescription': [
            "This field is required."
        ],
        'resumableHash': [
            "This field is required."
        ]
    }

    @pytest.mark.django_db
    def test_file_build_ok(
            self,
            test_client: APIClient,
            get_user: Callable[..., Any],
            get_token: Callable[..., Any],
            get_chunks: Callable[..., Any]
    ) -> None:

        user = get_user()
        url = reverse(FILE_BUILD_URL_NAME)
        url_query_params = get_chunks(user)
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.post(url + url_query_params)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_returns_400_if_query_params_missing(
            self,
            test_client: APIClient,
            get_user: Callable[..., Any],
            get_token: Callable[..., Any]
    ) -> None:

        user = get_user()
        url = reverse(FILE_BUILD_URL_NAME)
        test_client.credentials(HTTP_Authorization=get_token(user))

        response = test_client.post(url)
        data_to_assert = response.data.get('data')

        assert response.status_code == 400
        assert data_to_assert.get('error_detail')[0] == self.QUERY_PARAMS_ERROR_MESSAGE
