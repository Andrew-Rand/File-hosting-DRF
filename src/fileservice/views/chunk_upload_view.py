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
from src.fileservice.serializers.query_params_serializer import QueryParamsSerializer


def get_chunk_name(uploaded_filename: str, chunk_number: int) -> str:
    return f'{uploaded_filename}_part_{chunk_number}'


class ChunkUploadView(generics.GenericAPIView):

    temp_storage_path = FileStorage.objects.get(type='temp')

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = QueryParamsSerializer(data=request.query_params)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        identifier = serializer.validated_data.get('identifier')
        filename = serializer.validated_data.get('filename')
        chunk_number = serializer.validated_data.get('chunk_number')

        user_dir_path = os.path.join(self.temp_storage_path.destination, str(user.id))
        chunks_dir_path = os.path.join(user_dir_path, identifier)

        chunk_file = os.path.join(chunks_dir_path, get_chunk_name(filename, chunk_number))

        if os.path.isfile(chunk_file):
            return OkResponse()
        else:
            # Let resumable.js know this chunk does not exists and needs to be uploaded
            raise NotFoundError()

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = QueryParamsSerializer(data=request.query_params)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        identifier = serializer.validated_data.get('identifier')
        filename = serializer.validated_data.get('filename')
        chunk_number = serializer.validated_data.get('chunk_number')

        # get chunk data
        chunk_data = request.FILES.get('file')

        # make temp directory
        user_dir_path = os.path.join(self.temp_storage_path.destination, str(user.id))
        chunks_dir_path = os.path.join(user_dir_path, identifier)
        os.makedirs(chunks_dir_path, 0o777, exist_ok=True)

        # save chunk data
        chunk_name = get_chunk_name(filename, chunk_number)
        chunk_file = os.path.join(chunks_dir_path, chunk_name)

        with open(chunk_file, 'wb') as file:
            for chunk in chunk_data.chunks():
                file.write(chunk)

        return OkResponse()
