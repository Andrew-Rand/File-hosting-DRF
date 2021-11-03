from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.fileservice.serializers.file_serializer import FileSerializer
from src.basecore.custom_error_handler import NotFoundError, ForbiddenError
from src.fileservice.models import File


class FileDetailView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        if not File.objects.filter(id=self.kwargs['pk'], user=user).exists():
            raise NotFoundError('This file does not exist or doesn`t belong to this user')

        file = File.objects.get(id=self.kwargs['pk'])

        serializer_for_queryset = FileSerializer(instance=file)
        return Response(serializer_for_queryset.data)
