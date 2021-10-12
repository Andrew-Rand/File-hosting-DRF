from typing import Any

import jwt
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import create_token
from src.accounts.models import User
from src.basecore.custom_error_handler import BadAuthenticationError
from src.basecore.responses import OkResponse
from src.config.settings import SECRET_KEY
from src.accounts.constants import ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME


class RefreshView(generics.GenericAPIView):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        refresh_token = request.data.get("refresh")
        if refresh_token is None:
            raise BadAuthenticationError('Authentication credentials were not provided.')
        try:
            payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise BadAuthenticationError('expired refresh token, please login again.')
        except jwt.DecodeError:
            raise BadAuthenticationError('token data is incorrect')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise BadAuthenticationError('User not found')

        if not user.is_active:
            raise BadAuthenticationError('user is inactive')

        access_token = create_token(str(user.id), time_delta_seconds=ACCESS_TOKEN_LIFETIME)
        refresh_token = create_token(str(user.id), time_delta_seconds=REFRESH_TOKEN_LIFETIME)

        #  add tokens to response
        result_to_response = {
            'access-token': access_token,
            'refresh-token': refresh_token
        }
        #  add tokens to response
        return OkResponse(data=result_to_response)
