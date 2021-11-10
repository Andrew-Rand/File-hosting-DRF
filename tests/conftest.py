import pytest


@pytest.fixture
def test_client():
    from rest_framework.test import APIClient
    return APIClient()
