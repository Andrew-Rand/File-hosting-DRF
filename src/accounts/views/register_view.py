from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.serializers import UserSerializer
from src.basecore.std_response import create_std_response


class RegisterView(generics.GenericAPIView):

    permission_classes = [AllowAny, ]

    def post(self, request: Request) -> Response:

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(create_std_response(result=serializer.data))
        # return Response(serializer.data)
