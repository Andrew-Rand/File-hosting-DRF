from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.basecore.std_response import create_std_response


class AuthView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response(create_std_response(result={"is login?": "yes"}))
