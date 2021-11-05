from typing import Any

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.accounts.serializers.user_detail_serializer import UserDetailSerializer
from src.basecore.responses import OkResponse


class UserDetailView(generics.GenericAPIView):

    serializer_class = UserDetailSerializer

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = self.get_serializer(instance=user)
        return Response(serializer.data)

    @login_required
    def patch(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = self.get_serializer(data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.update(instance=user, validated_data=serializer.validated_data)
        return OkResponse(data=serializer.validated_data)
