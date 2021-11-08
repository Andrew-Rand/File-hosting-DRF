from typing import Any

from rest_framework import status, serializers
from rest_framework.response import Response

from src.basecore.std_response import create_std_response


class BadRequestError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args)


class ForbiddenError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args)


class NotAuthorizedError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args)


class NotFoundError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args)


class TeapotError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args)


class NoContent(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args)


def error_handler(exc: Exception, context: Any) -> Response:

    if isinstance(exc, BadRequestError):
        return Response(create_std_response(error_detail=exc.args), status=status.HTTP_400_BAD_REQUEST)

    elif isinstance(exc, ForbiddenError):
        return Response(create_std_response(error_detail=exc.args), status=status.HTTP_403_FORBIDDEN)

    elif isinstance(exc, serializers.ValidationError):
        return Response(create_std_response(error_detail=exc.args), status=status.HTTP_400_BAD_REQUEST)

    elif isinstance(exc, NotAuthorizedError):
        return Response(create_std_response(error_detail=exc.args), status=status.HTTP_401_UNAUTHORIZED)

    elif isinstance(exc, NotFoundError):
        return Response(create_std_response(error_detail=exc.args), status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, TeapotError):
        return Response(create_std_response(error_detail=exc.args), status=status.HTTP_418_IM_A_TEAPOT)

    elif isinstance(exc, NoContent):
        return Response(create_std_response(error_detail=exc.args), status=status.HTTP_204_NO_CONTENT)
