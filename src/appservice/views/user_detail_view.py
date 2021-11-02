from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.appservice.serializers.user_detail_serializer import UserDetailSerializer
from src.basecore.custom_error_handler import NotFoundError
from src.basecore.responses import OkResponse


class UserDetailView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        try:
            user = User.objects.get(id=user.id)
        except User.DoesNotExist:
            raise NotFoundError('This user does not exist')
        serializer_for_queryset = UserDetailSerializer(instance=user)
        return Response(serializer_for_queryset.data)

    @login_required
    def patch(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        try:
            user = User.objects.get(id=user.id)
        except User.DoesNotExist:
            raise NotFoundError('This user does not exist')
        serializer = UserDetailSerializer(data=request.data, partial=True)
        serializer.save()
        return OkResponse(data=serializer.data)
