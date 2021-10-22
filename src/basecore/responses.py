from typing import Dict, Any

from rest_framework.response import Response
from rest_framework import status
from src.basecore.std_response import create_std_response


class OkResponse(Response):
    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__(create_std_response(result=data), status=status.HTTP_200_OK)


class CreatedResponse(Response):
    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__(create_std_response(result=data), status=status.HTTP_201_CREATED)
