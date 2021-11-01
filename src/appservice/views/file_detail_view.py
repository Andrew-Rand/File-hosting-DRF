from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.appservice.serializers.file_serializer import FileSerializer
from src.basecore.custom_error_handler import NotFoundError
from src.fileservice.models import File


class FileDetailView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        queryset = File.objects.get(id=self.kwargs['pk'])
        print(queryset)
        if not queryset.user == user:
            raise NotFoundError()
        serializer_for_queryset = FileSerializer(instance=queryset)
        return Response(serializer_for_queryset.data)
