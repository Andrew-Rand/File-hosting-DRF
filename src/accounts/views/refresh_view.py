from typing import Any

import jwt
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import create_token
from src.accounts.models import User
from src.basecore.custom_error_handler import ForbiddenError, NotFoundError, NotAuthorizedError
from src.basecore.responses import OkResponse
from src.config.settings import SECRET_KEY
from src.accounts.constants import ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME


class RefreshView(generics.GenericAPIView):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        refresh_token = request.data.get("refresh")
        if refresh_token is None:
            raise ForbiddenError('Authentication credentials were not provided.')
        try:
            payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise NotAuthorizedError('expired refresh token, please login again.')
        except jwt.DecodeError:
            raise NotAuthorizedError('token data is incorrect')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise NotFoundError('User not found')

        access_token = create_token(str(user.id), time_delta_seconds=ACCESS_TOKEN_LIFETIME)
        refresh_token = create_token(str(user.id), time_delta_seconds=REFRESH_TOKEN_LIFETIME)

        #  add tokens to response
        response_data = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        #  add tokens to response
        return OkResponse(data=response_data)
