from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import jwt_auth
from src.basecore.responses import OkResponse


class AuthView(generics.GenericAPIView):

    @jwt_auth
    def get(self, request: Request) -> Response:
        result_to_response = {"is login?": "yes"}
        return OkResponse(data=result_to_response)
