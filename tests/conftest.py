import os
from typing import Callable, Any

import pytest
from rest_framework.test import APIClient

from src.accounts.authentication import create_token
from src.accounts.constants import ACCESS_TOKEN_LIFETIME
from src.accounts.models import User
from src.fileservice.utils import calculate_hash_md5
from src.fileservice.models import File
from src.fileservice.models import FileStorage
from src.fileservice.models.file_storage import PERMANENT_STORAGE


@pytest.fixture
def test_client() -> APIClient:
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def get_user() -> Callable:
    def create_user(**kwargs: Any) -> User:

        username = kwargs.get('username', 'test_username')
        password = kwargs.get('password', '1234Abc%%%')
        email = kwargs.get('email', 'test@mail.ru')

        return User.objects.create_user(
            username=username,
            password=password,
            email=email,
            **kwargs
        )
    return create_user


@pytest.fixture
def get_token() -> Callable:
    def make_token(user: User) -> str:
        token = create_token(user_id=str(user.id), time_delta_seconds=ACCESS_TOKEN_LIFETIME)
        return token
    return make_token


@pytest.fixture
def get_file() -> Callable:
    def make_file(user: User) -> File:
        permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)
        os.mkdir(f'storage/permanent/{user.id}')
        test_file_path = f'storage/permanent/{user.id}/test_file.txt'
        test_file = open(test_file_path, 'w')
        test_file.close()

        file_hash = calculate_hash_md5(test_file_path)

        File.create_model_object(user=user,
                                 hash=file_hash,
                                 storage=permanent_storage,
                                 destination=f'{user.id}/test_file.txt',
                                 data={'filename': 'test_file.txt',
                                       'type': '.txt',
                                       'total_size': 48
                                       })

        file = File.objects.filter(user=user).first()

        return file
    return make_file


@pytest.fixture
def get_chunks() -> Callable:
    def make_chunks(user: User) -> str:
        user_chunks_path = f'storage/temp/{user.id}/148-test_chunktxt/'
        os.makedirs(user_chunks_path, 0o777, exist_ok=True)
        test_file_path = f'{user_chunks_path}test_chunk.txt_part_1'
        test_chunk = open(test_file_path, 'w')
        test_chunk.close()
        return '?resumableChunkNumber=1&resumableChunkSize=52428800&resumableCurrentChunkSize=148&' \
               'resumableTotalSize=148&resumableType=text%2Fplain&resumableIdentifier=148-test_chunktxt&' \
               'resumableFilename=test_chunk.txt&resumableRelativePath=test_chunk.txt&resumableTotalChunks=1' \
               '&resumableDescription=description&resumableHash=51111111111'
    return make_chunks
