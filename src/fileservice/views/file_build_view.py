import os
from typing import Any, List

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
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

    queryset_temp = FileStorage.objects.get(type='temp')
    temp_storage_path = queryset_temp.destination

    queryset_perm = FileStorage.objects.get(type='permanent')
    permanent_storage_path = queryset_perm.destination

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        query = UploadDataSerializer(request.query_params)

        # if not query.is_valid():
        #     raise ValidationError(query.errors)

        identifier = query.data.get("identifier")
        filename = query.data.get("filename")
        total_chunks = query.data.get("total_chunks")

        # make temp directory
        temp_dir = os.path.join(FileBuildView.temp_storage_path, identifier)

        # check if the upload is complete
        chunk_paths = [
            os.path.join(temp_dir, get_chunk_name(filename, x))
            for x in range(1, total_chunks + 1)
        ]
        upload_complete = all([os.path.exists(p) for p in chunk_paths])

        # create final file from all chunks
        if upload_complete:
            if not os.path.isdir(FileBuildView.permanent_storage_path):
                os.makedirs(FileBuildView.permanent_storage_path, 0o777)

            target_file_name = os.path.join(FileBuildView.permanent_storage_path, filename)
            build_file(target_file_name, chunk_paths)
            os.rmdir(temp_dir)

            #  calculate hash for database field
            hash = calculate_hash_md5(target_file_name)

            # add information about file in files db (EXAMPLE)
            filetype = request.query_params.get('resumableType')
            filesize = request.query_params.get('resumableTotalSize')

            file = File()

            file.user = user
            file.name = filename
            file.type = filetype
            file.storage = FileBuildView.queryset_perm
            file.destination = target_file_name
            file.hash = hash
            file.size = filesize

            file.save()
            #  ^you can do it with File.create()^

        return CreatedResponse(data={"file saved in": temp_dir})
