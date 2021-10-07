from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required


class AuthView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request) -> Response:
        return Response({"is login?": "yes"})
