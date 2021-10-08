from typing import Any

import jwt
from rest_framework import exceptions, generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import create_token
from src.accounts.models import User
from src.config.settings import SECRET_KEY


ACCESS_TOKEN_LIFETIME = 1200  # 20 minutes for access token
REFRESH_TOKEN_LIFETIME = 432000  # 5 days for refresh token


class RefreshView(generics.GenericAPIView):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        try:
            authorization_header = request.headers.get('Authorization')
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=['HS256'])
            raise exceptions.AuthenticationFailed('Access token is still alive, you don`t need refresh')
        except jwt.ExpiredSignatureError:
            refresh_token = request.headers.get('refresh_token')
            if refresh_token is None:
                raise exceptions.AuthenticationFailed(
                    'Authentication credentials were not provided.')
            try:
                payload = jwt.decode(
                    refresh_token, SECRET_KEY, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed(
                    'expired refresh token, please login again.')

            user = User.objects.filter(id=payload['id']).first()
            if user is None:
                raise exceptions.AuthenticationFailed('User not found')

            if not user.is_active:
                raise exceptions.AuthenticationFailed('user is inactive')

            access_token = create_token(str(user.id), time_delta_seconds=ACCESS_TOKEN_LIFETIME)
            refresh_token = create_token(str(user.id), time_delta_seconds=REFRESH_TOKEN_LIFETIME)

            #  add tokens to response
            response = Response()
            response.data = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            return response
