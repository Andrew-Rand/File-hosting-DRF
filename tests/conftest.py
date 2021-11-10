import pytest

from src.accounts.authentication import create_token
from src.accounts.constants import ACCESS_TOKEN_LIFETIME
from src.accounts.models import User
from src.fileservice.utils import calculate_hash_md5
from tests.constants import TEST_USERNAME, TEST_EMAIL, TEST_PASSWORD, TEST_FILE_PATH, TEST_FILE_DATA


@pytest.fixture
def test_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def create_user_with_token():
    user = User.objects.create_user(username=TEST_USERNAME, email=TEST_EMAIL, password=TEST_PASSWORD)
    token = create_token(str(user.id), time_delta_seconds=ACCESS_TOKEN_LIFETIME)
    return user, token


@pytest.fixture
def get_file_hash():
    test_file = open(TEST_FILE_PATH, 'w')
    test_file.close()
    file_hash = calculate_hash_md5(TEST_FILE_PATH)
    return file_hash


@pytest.fixture
def file_create(create_user_with_token, get_file_hash):
    from src.fileservice.models import File
    from src.fileservice.models import FileStorage
    from src.fileservice.models.file_storage import PERMANENT_STORAGE

    permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)
    File.create_model_object(user=create_user_with_token[0],
                                    hash=get_file_hash,
                                    storage=permanent_storage,
                                    destination=TEST_FILE_PATH,
                                    data=TEST_FILE_DATA)
    file = File.objects.filter(user=create_user_with_token[0]).first()
    return file
