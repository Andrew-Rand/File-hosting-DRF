from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, serializers

from src.accounts.authentication import create_token
from src.accounts.serializers.user_login_serializer import UserLoginSerializer


class LoginView(generics.GenericAPIView):

    def post(self, request: Request) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            raise serializers.ValidationError('Authentication failed')
        user_id = serializer.data.get('id')
        access_token = create_token(user_id, time_delta_days=1)
        refresh_token = create_token(user_id, time_delta_days=30)

        #  add tokens to response
        response = Response()
        response.data = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return response
