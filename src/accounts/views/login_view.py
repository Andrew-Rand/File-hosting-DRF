from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, serializers

from src.accounts.authentication import create_token
from src.accounts.serializers import UserLoginSerializer


class LoginView(generics.GenericAPIView):

    permission_classes = [AllowAny, ]

    def post(self, request: Request) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            raise serializers.ValidationError('Auth f**k')
        user_id = serializer.data.get('id')
        access_token = create_token(user_id, time_delta_days=1)
        refresh_token = create_token(user_id, time_delta_days=30)

        #  add tokens to response
        response = Response()
        response.data = {
            'access-token': access_token,
            'refresh-token': refresh_token
        }
        return response
