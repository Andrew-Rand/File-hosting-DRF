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
from src.fileservice.serializers.upload_data_serializer import UploadDataSerializer
from src.fileservice.views.file_upload_view import get_chunk_name


def build_file(target_file_name: str, chunk_paths: List[str]) -> None:
    with open(target_file_name, "ab") as target_file:
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

        query = UploadDataSerializer(data=request.query_params)

        if not query.is_valid():
            raise ValidationError(query.errors)

        identifier = query.data.get('resumableIdentifier')
        filename = query.data.get('resumableFilename')
        total_chunks = query.data.get('resumableTotalChunks')

        # make temp directory
        chunks_dir_path = os.path.join(FileBuildView.temp_storage_path.destination, identifier)

        # check if the upload is complete
        chunk_paths = [
            os.path.join(chunks_dir_path, get_chunk_name(filename, x))
            for x in range(1, total_chunks + 1)
        ]
        upload_complete = all([os.path.exists(p) for p in chunk_paths])

        if not upload_complete:
            raise BadRequestError

        # create final file from all chunks
        user_storage_path = os.path.join(FileBuildView.permanent_storage_path.destination, str(user.id))
        os.makedirs(user_storage_path, 0o777)

        target_file_name = os.path.join(user_storage_path, filename)
        build_file(target_file_name, chunk_paths)
        os.rmdir(chunks_dir_path)

        #  calculate hash for database field
        hash = calculate_hash_md5(target_file_name)

        # add information about file in files db
        filetype = query.data.get('resumableType')
        filesize = query.data.get('resumableTotalSize')

        file = File()

        file.user = user
        file.name = filename
        file.type = filetype
        file.storage = FileBuildView.permanent_storage_path
        file.destination = target_file_name
        file.hash = hash
        file.size = filesize

        file.save()
        #  ^you can do it with File.create()^

        return CreatedResponse(data={'file saved in': user_storage_path})
