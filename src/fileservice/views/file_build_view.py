import os
from typing import Any, List

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.responses import CreatedResponse
from src.fileservice.models.file_storage import TEMP_STORAGE, PERMANENT_STORAGE
from src.fileservice.utils import build_file_from_chunks
from src.fileservice.models import FileStorage
from src.fileservice.serializers.file_upload_parameters_serializer import FileUploadParametersSerializer


class FileBuildView(generics.GenericAPIView):

    temp_storage = FileStorage.objects.get(type=TEMP_STORAGE)
    permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)
    serializer_class = FileUploadParametersSerializer

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = self.get_serializer(data=request.query_params)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        build_file_from_chunks(user, self.temp_storage, self.permanent_storage, serializer)

        return CreatedResponse(data=serializer.data)
