from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.basecore.custom_error_handler import BadRequestError


class RaiseView(generics.GenericAPIView):

    def get(self, request: Request) -> Response:
        raise BadRequestError
