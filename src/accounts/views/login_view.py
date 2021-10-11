from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics

from src.accounts.authentication import create_token
from src.accounts.serializers import UserLoginSerializer
from src.basecore.responses import OkResponse
from src.basecore.std_response import create_std_response


class LoginView(generics.GenericAPIView):

    permission_classes = [AllowAny, ]

    def post(self, request: Request) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.data.get('id')
        access_token = create_token(user_id, 1)
        refresh_token = create_token(user_id, 30)

        result_to_response = {
            'access-token': access_token,
            'refresh-token': refresh_token
        }
        #  add tokens to response
        return OkResponse(data=result_to_response)

