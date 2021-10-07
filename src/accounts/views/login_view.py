from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, serializers

from src.accounts.authentication import create_token
from src.accounts.serializers.user_login_serializer import UserLoginSerializer
from src.basecore.responses import OkResponse


ACCESS_TOKEN_LIFETIME = 1200  # 20 minutes for access token
REFRESH_TOKEN_LIFETIME = 432000  # 5 days for refresh token


class LoginView(generics.GenericAPIView):

    def post(self, request: Request) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            raise serializers.ValidationError('Authentication failed')
        user_id = serializer.data.get('id')
        access_token = create_token(user_id, time_delta_seconds=ACCESS_TOKEN_LIFETIME)
        refresh_token = create_token(user_id, time_delta_seconds=REFRESH_TOKEN_LIFETIME)

        result_to_response = {
            'access-token': access_token,
            'refresh-token': refresh_token
        }
        #  add tokens to response
        return OkResponse(data=result_to_response)

