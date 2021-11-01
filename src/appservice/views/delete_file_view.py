from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.appservice.serializers.file_delete_serializer import FileDeleteSerializer
from src.appservice.serializers.file_serializer import FileSerializer
from src.basecore.custom_error_handler import NotFoundError
from src.basecore.responses import OkResponse
from src.fileservice.models import File


class DeleteFileView(generics.GenericAPIView):

    @login_required
    def put(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        file = File.objects.get(id=self.kwargs['pk'])
        if not file.user == user:
            raise NotFoundError()
        file.is_alive = False
        file.save()
        return OkResponse({})
