import os
from typing import Tuple

import pytest
from rest_framework.test import APIClient

from src.accounts.authentication import create_token
from src.accounts.constants import ACCESS_TOKEN_LIFETIME
from src.accounts.models import User
from src.fileservice.models import File
from src.fileservice.utils import calculate_hash_md5
from tests.constants import TEST_USERNAME, TEST_EMAIL, TEST_PASSWORD, TEST_STORAGE_PATH, TEST_FILE_DATA,\
    TEST_FILE_NAME, TEST_FILE_TYPE, TEST_CHUNK_PATH, TEST_CHUNK_NAME, TEST_QUERYSET_FOR_BUILD


@pytest.fixture
def test_client() -> APIClient:
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def create_user_and_get_token() -> Tuple[User, str]:
    user = User.objects.create_user(username=TEST_USERNAME, email=TEST_EMAIL, password=TEST_PASSWORD)
    token = create_token(str(user.id), time_delta_seconds=ACCESS_TOKEN_LIFETIME)
    return user, token


@pytest.fixture
def file_create(create_user_and_get_token: Tuple[User, str]) -> File:
    from src.fileservice.models import File
    from src.fileservice.models import FileStorage
    from src.fileservice.models.file_storage import PERMANENT_STORAGE

    permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)
    user = create_user_and_get_token[0]
    os.mkdir(f'{TEST_STORAGE_PATH}/{user.id}')
    test_file_path = f'{TEST_STORAGE_PATH}/{user.id}/{TEST_FILE_NAME}{TEST_FILE_TYPE}'
    test_file = open(test_file_path, 'w')
    test_file.close()

    file_hash = calculate_hash_md5(test_file_path)

    File.create_model_object(user=user,
                             hash=file_hash,
                             storage=permanent_storage,
                             destination=f'{user.id}/{TEST_FILE_NAME}{TEST_FILE_TYPE}',
                             data=TEST_FILE_DATA)

    file = File.objects.filter(user=create_user_and_get_token[0]).first()

    return file


@pytest.fixture
def chunks_create(create_user_and_get_token) -> str:
    user = create_user_and_get_token[0]
    user_chunks_path = f'{TEST_CHUNK_PATH}/{user.id}/148-test_chunktxt/'
    os.makedirs(user_chunks_path, 0o777, exist_ok=True)
    test_file_path = f'{user_chunks_path}{TEST_CHUNK_NAME}'
    test_chunk = open(test_file_path, 'w')
    test_chunk.close()
    return TEST_QUERYSET_FOR_BUILD
