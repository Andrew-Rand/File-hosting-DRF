from typing import Any
from uuid import UUID

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.responses import OkResponse
from src.fileservice.serializers.file_serializer import FileSerializer
from src.basecore.custom_error_handler import NotFoundError
from src.fileservice.models import File


class FileView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, pk: UUID, *args: Any, user: User, **kwargs: Any) -> Response:

        file = File.objects.filter(id=pk, user=user).first()
        if not file:
            raise NotFoundError('File not found')

        serializer = FileSerializer(instance=file)
        return Response(serializer.data)

    @login_required
    def patch(self, request: Request, pk: UUID, *args: Any, user: User, **kwargs: Any) -> Response:

        file = File.objects.filter(id=pk, user=user).first()
        if not file:
            raise NotFoundError('File not found')

        file.description = request.data.get('description')
        file.save()
        return OkResponse({})

    @login_required
    def delete(self, request: Request, pk: UUID, *args: Any, user: User, **kwargs: Any) -> Response:

        file = File.objects.filter(id=pk, user=user).first()
        if not file:
            raise NotFoundError('File not found')
        file.delete()
        return OkResponse({})
