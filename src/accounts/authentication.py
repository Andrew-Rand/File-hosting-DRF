import jwt
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import exceptions
from rest_framework.request import Request

from src.config.settings import SECRET_KEY


def jwt_auth(func):
    def wrapper(request_object, request: Request, *args, **kwargs):
        User = get_user_model()
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return HttpResponse('No token')
        try:
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(
                access_token, SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')
        return func(request_object, request, *args, **kwargs)
    return wrapper
