import pytest

from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_user_create() -> None:

    User = get_user_model()
    # user_data = {'first_name': 'test_name',
    #              'last_name': 'test_lname',
    #              'email': 'test_email@gmail.ru',
    #              'password': '1111',
    #              'username': 'aaaa'}

    User.objects.create()
    assert User.objects.count() == 1
