from typing import Any

from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics

from src.accounts.authentication import create_token
from src.accounts.serializers.user_login_serializer import UserLoginSerializer
from src.accounts.constants import ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME


class LoginView(generics.GenericAPIView):

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        user_id = serializer.data.get('id')
        access_token = create_token(user_id, time_delta_seconds=ACCESS_TOKEN_LIFETIME)
        refresh_token = create_token(user_id, time_delta_seconds=REFRESH_TOKEN_LIFETIME)

        #  add tokens to response
        response = Response()
        response.data = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return response
