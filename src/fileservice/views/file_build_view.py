import os
from typing import Any, List

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.custom_error_handler import BadRequestError
from src.basecore.responses import CreatedResponse
from src.fileservice.calculate_hash import calculate_hash_md5
from src.fileservice.models import FileStorage, File
from src.fileservice.serializers.query_params_serializer import QueryParamsSerializer
from src.fileservice.views.chunk_upload_view import get_chunk_name


def build_file(target_file_name: str, chunk_paths: List[str]) -> None:
    with open(target_file_name, 'ab') as target_file:
        for stored_chunk_file_name in chunk_paths:
            stored_chunk_file = open(stored_chunk_file_name, 'rb')
            target_file.write(stored_chunk_file.read())
            stored_chunk_file.close()
            os.unlink(stored_chunk_file_name)
    target_file.close()


class FileBuildView(generics.GenericAPIView):

    temp_storage_path = FileStorage.objects.get(type='temp')
    permanent_storage_path = FileStorage.objects.get(type='permanent')

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = QueryParamsSerializer(data=request.query_params)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        identifier = serializer.validated_data.get('identifier')
        filename = serializer.validated_data.get('filename')
        total_chunks = serializer.validated_data.get('total_chunk')
        filetype = serializer.validated_data.get('type')
        filesize = serializer.validated_data.get('total_size')

        # make temp directory
        chunks_dir_path = os.path.join(self.temp_storage_path.destination, identifier)

        # check if the upload is complete
        chunk_paths = [
            os.path.join(chunks_dir_path, get_chunk_name(filename, x))
            for x in range(1, total_chunks + 1)
        ]
        upload_complete = all([os.path.exists(p) for p in chunk_paths])

        if not upload_complete:
            raise BadRequestError('There aren`t all chunks for this file. Try to continue upload chunks')

        # create final file from all chunks
        user_storage_path = os.path.join(self.permanent_storage_path.destination, str(user.id))
        os.makedirs(user_storage_path, 0o777, exist_ok=True)
        target_file_name = os.path.join(user_storage_path, filename)
        build_file(target_file_name, chunk_paths)
        os.rmdir(chunks_dir_path)

        file_hash = calculate_hash_md5(target_file_name)

        File.objects.create(user=user, name=filename, type=filetype, storage=self.permanent_storage_path,
                            destination=target_file_name, hash=file_hash, size=filesize)

        return CreatedResponse(data={'file saved in': user_storage_path})
