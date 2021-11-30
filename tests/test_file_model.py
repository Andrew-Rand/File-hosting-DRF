from typing import Callable, Any

import pytest

from src.config.settings import INSTALLED_APPS
from src.fileservice.models import File, FileStorage
from src.fileservice.models.file_storage import PERMANENT_STORAGE


class TestSettings:

    def test_fileservice_is_configured(self) -> None:

        assert 'src.fileservice' in INSTALLED_APPS


class TestUserModel:

    @pytest.mark.django_db
    def test_file_create(self, get_user: Callable[..., Any], get_file: Callable[..., Any]) -> None:

        user = get_user()
        get_file(user)

        assert File.objects.count() == 1

    @pytest.mark.django_db
    def test_user_owner_file(self, get_user: Callable[..., Any], get_file: Callable[..., Any]) -> None:

        user = get_user()
        file = get_file(user)

        file_obj = File.objects.get(id=file.id)

        assert file_obj.user == user

    @pytest.mark.django_db
    def test_get_absolute_path(self, get_user: Callable[..., Any], get_file: Callable[..., Any]) -> None:

        user = get_user()
        file = get_file(user)

        file_obj = File.objects.get(id=file.id)
        permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)

        assert file_obj.absolute_path == f'{permanent_storage.destination}/{user.id}/test_file.txt'

    @pytest.mark.django_db
    def test_file_default_description(self, get_user: Callable[..., Any], get_file: Callable[..., Any]) -> None:

        user = get_user()
        file = get_file(user)

        file_obj = File.objects.get(id=file.id)

        assert file_obj.description is None
