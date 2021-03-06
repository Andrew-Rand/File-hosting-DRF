from typing import Dict, Any

from rest_framework.response import Response
from rest_framework import status
from src.basecore.std_response import create_std_response


class OkResponse(Response):
    def __init__(self, data: Dict[str, Any], total_count: int = 0) -> None:
        super().__init__(create_std_response(result=data, total_count=total_count), status=status.HTTP_200_OK)


class CreatedResponse(Response):
    def __init__(self, data: Dict[str, Any], total_count: int = 0) -> None:
        super().__init__(create_std_response(result=data, total_count=total_count), status=status.HTTP_201_CREATED)
