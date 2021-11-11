from typing import Tuple

import pytest

from src.accounts.models import User
from src.config.settings import INSTALLED_APPS
from src.fileservice.models import File, FileStorage
from src.fileservice.models.file_storage import PERMANENT_STORAGE
from tests.constants import TEST_FILE_NAME, TEST_FILE_TYPE


class TestSettings:

    def test_fileservice_is_configured(self) -> None:

        assert 'src.fileservice' in INSTALLED_APPS


class TestUserModel:

    @pytest.mark.django_db
    def test_file_create(self, file_create: File) -> None:

        assert File.objects.count() == 1

    @pytest.mark.django_db
    def test_user_owner_file(self, file_create: File, create_user_and_get_token: Tuple[User, str]) -> None:
        file_obj = File.objects.get(id=file_create.id)
        user_obj = create_user_and_get_token[0]

        assert file_obj.user == user_obj

    @pytest.mark.django_db
    def test_get_absolute_path(self, file_create: File, create_user_and_get_token: Tuple[User, str]) -> None:
        file_obj = File.objects.get(id=file_create.id)
        user_obj = create_user_and_get_token[0]
        permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)

        assert file_obj.absolute_path == f'{permanent_storage.destination}/' \
                                         f'{user_obj.id}/{TEST_FILE_NAME}{TEST_FILE_TYPE}'

    @pytest.mark.django_db
    def test_user_default_edit(self, file_create: File) -> None:
        file_obj = File.objects.get(id=file_create.id)
        assert file_obj.description is None
