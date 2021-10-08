import datetime
from typing import Any, Callable

import jwt
from django.http import HttpResponse
from rest_framework import exceptions
from rest_framework.request import Request

from src.accounts.models import User
from src.config.settings import SECRET_KEY


def create_token(user_id: str, time_delta_seconds: int = 1) -> str:
    token_payload = {
        'id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=time_delta_seconds),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
    return token


def login_required(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(request_object: object, request: Request, *args: Any, **kwargs: Any) -> Any:
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return HttpResponse('No token')
        try:
            access_token = authorization_header
            payload = jwt.decode(
                access_token, SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(id=payload['id']).first()
        print(payload)
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')
        return func(request_object, request, *args, **kwargs)
    return wrapper
