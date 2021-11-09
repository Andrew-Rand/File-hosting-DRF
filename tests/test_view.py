import pytest

from django.urls import reverse


@pytest.fixture
def test_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_unauthorized_request(test_client):
    url = reverse('user_detail')
    response = test_client.get(url)
    assert response.status_code == 403
