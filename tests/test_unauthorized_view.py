import pytest

from django.urls import reverse


class TestUnauthorizedRequest:

    @pytest.mark.django_db
    def test_unauthorized_user_detail(self, test_client):
        url = reverse('user_detail')
        response = test_client.get(url)
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_unauthorized_chunk_upload(self, test_client):
        url = reverse('chunk_upload')
        response = test_client.get(url)
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_unauthorized_download_all_file_as_zip(self, test_client):
        url = reverse('download_all_file_as_zip')
        response = test_client.get(url)
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_unauthorized_all_user_files(self, test_client):
        url = reverse('all_user_files')
        response = test_client.get(url)
        assert response.status_code == 403
