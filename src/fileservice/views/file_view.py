from typing import Any
from uuid import UUID

from django.core.exceptions import ValidationError
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.responses import OkResponse
from src.fileservice.serializers.file_serializer import FileSerializer
from src.basecore.custom_error_handler import NotFoundError, NoContent
from src.fileservice.models import File


class FileView(generics.GenericAPIView):

    serializer_class = FileSerializer

    @login_required
    def get(self, request: Request, pk: UUID, *args: Any, user: User, **kwargs: Any) -> Response:

        file_obj = File.objects.filter(id=pk, user=user).first()
        if not file_obj:
            raise NotFoundError('File not found')

        serializer = self.get_serializer(instance=file_obj)
        return Response(serializer.data)

    @login_required
    def patch(self, request: Request, pk: UUID, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = self.get_serializer(data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        file_obj = File.objects.filter(id=pk, user=user).first()
        if not file_obj:
            raise NotFoundError('File not found')

        serializer.update(instance=file_obj, validated_data=serializer.validated_data)
        return OkResponse({})

    @login_required
    def delete(self, request: Request, pk: UUID, *args: Any, user: User, **kwargs: Any) -> Response:

        file_obj = File.objects.filter(id=pk, user=user).first()
        if not file_obj:
            raise NoContent('File not found')
        file_obj.delete()
        return OkResponse({})
