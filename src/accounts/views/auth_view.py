from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from ..authentication import jwt_auth


class AuthView(generics.GenericAPIView):

    @jwt_auth
    def get(self, request: Request) -> Response:
        return Response({"is login?": "yes"})
