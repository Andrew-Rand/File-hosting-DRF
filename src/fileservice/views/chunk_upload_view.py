import os
from typing import Any

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.custom_error_handler import NotFoundError
from src.basecore.responses import OkResponse
from src.fileservice.models import FileStorage
from src.fileservice.models.file_storage import TEMP_STORAGE, PERMANENT_STORAGE
from src.fileservice.serializers.file_upload_parameters_serializer import FileUploadParametersSerializer
from src.fileservice.utils import make_chunk_dir_path


def get_chunk_name(uploaded_filename: str, chunk_number: int) -> str:
    return f'{uploaded_filename}_part_{chunk_number}'


class ChunkUploadView(generics.GenericAPIView):

    temp_storage = FileStorage.objects.get(type=TEMP_STORAGE)
    permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)
    serializer_class = FileUploadParametersSerializer

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        filename = serializer.validated_data.get('filename')
        chunk_number = serializer.validated_data.get('chunk_number')

        chunks_dir_path = make_chunk_dir_path(self.temp_storage.destination, str(user.id), serializer.validated_data)

        chunk_file = os.path.join(chunks_dir_path, get_chunk_name(filename, chunk_number))

        if os.path.isfile(chunk_file):
            return OkResponse({})
        # Let resumable.js know this chunk does not exists and needs to be uploaded
        raise NotFoundError()

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        filename = serializer.validated_data.get('filename')
        chunk_number = serializer.validated_data.get('chunk_number')

        # get chunk data
        chunk_data = request.FILES.get('file')

        # make temp directory
        chunks_dir_path = make_chunk_dir_path(self.temp_storage.destination, str(user.id), serializer.validated_data)
        os.makedirs(chunks_dir_path, 0o777, exist_ok=True)

        # save chunk data
        chunk_name = get_chunk_name(filename, chunk_number)
        chunk_file_path = os.path.join(chunks_dir_path, chunk_name)

        with open(chunk_file_path, 'wb') as file:
            for chunk in chunk_data.chunks():
                file.write(chunk)
        return OkResponse({})
