from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.basecore.responses import OkResponse


class AuthView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response_data = {"is login?": "yes"}
        return OkResponse(data=response_data)
