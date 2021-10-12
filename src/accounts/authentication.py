import datetime
from typing import Any, Callable

import jwt
from rest_framework.request import Request
from src.accounts.models import User
from src.basecore.custom_error_handler import BadAuthenticationError
from src.config.settings import SECRET_KEY


def create_token(user_id: str, time_delta_seconds: int) -> str:
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
            raise BadAuthenticationError('No token')
        try:
            access_token = authorization_header
            payload = jwt.decode(
                access_token, SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise BadAuthenticationError('access_token expired')
        except IndexError:
            raise BadAuthenticationError('Token prefix missing')
        except jwt.DecodeError:
            raise BadAuthenticationError('token data is incorrect')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise BadAuthenticationError('User not found')

        if not user.is_active:
            raise BadAuthenticationError('user is inactive')
        return func(request_object, request, *args, **kwargs)
    return wrapper
