from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import jwt_auth
from src.basecore.std_response import create_std_response


class AuthView(generics.GenericAPIView):

    @jwt_auth
    def get(self, request: Request) -> Response:
        return Response(create_std_response(result={"is login?": "yes"}))
