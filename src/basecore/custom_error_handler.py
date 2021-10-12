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


def error_handler(exc: Exception, context: Any) -> Response:

    if isinstance(exc, BadRequestError):
        return Response(create_std_response(status_code=status.HTTP_400_BAD_REQUEST, info=exc.args))

    elif isinstance(exc, ForbiddenError):
        return Response(create_std_response(status_code=status.HTTP_403_FORBIDDEN, info=exc.args))

    elif isinstance(exc, serializers.ValidationError):
        return Response(create_std_response(status_code=status.HTTP_400_BAD_REQUEST, info=exc.args))

    elif isinstance(exc, NotAuthorizedError):
        return Response(create_std_response(status_code=status.HTTP_401_UNAUTHORIZED, info=exc.args))

    elif isinstance(exc, NotFoundError):
        return Response(create_std_response(status_code=status.HTTP_404_NOT_FOUND, info=exc.args))

    elif isinstance(exc, TeapotError):
        return Response(create_std_response(status_code=status.HTTP_418_IM_A_TEAPOT, info=exc.args))
