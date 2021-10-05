from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.serializers.user_serializer import UserSerializer
from src.basecore.std_response import create_std_response


class RegisterView(generics.GenericAPIView):

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(create_std_response(result=serializer.data))
        # return Response(serializer.data)
