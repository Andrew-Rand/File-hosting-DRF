import os
from typing import Any

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.basecore.custom_error_handler import NotFoundError
from src.basecore.responses import OkResponse
from src.fileservice.serializers.upload_data_serializer import UploadDataSerializer


def get_chunk_name(uploaded_filename: str, chunk_number: int) -> str:
    return f'{uploaded_filename}_part_{chunk_number}'


class FileUploadView(generics.GenericAPIView):

    temp_base = os.path.expanduser("storage/temp/uploads")
    # temp_base = FileStorage.objects.filter(type='temp').first()

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:

        query = UploadDataSerializer(request.query_params)

        # if not query.is_valid():
        #     raise ValidationError(query.errors)

        identifier = query.data.get("identifier")
        filename = query.data.get("filename")
        chunk_number = query.data.get("chunk_number")

        temp_dir = os.path.join(FileUploadView.temp_base, identifier)

        chunk_file = os.path.join(temp_dir, get_chunk_name(filename, chunk_number))

        if os.path.isfile(chunk_file):
            return OkResponse(data={"ok?": "ok"})
        else:
            # Let resumable.js know this chunk does not exists and needs to be uploaded
            raise NotFoundError()

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:

        query = UploadDataSerializer(request.query_params)

        # if not query.is_valid():
        #     raise ValidationError(query.errors)

        identifier = query.data.get("identifier")
        filename = query.data.get("filename")
        chunk_number = query.data.get("chunk_number")

        # get chunk data
        chunk_data = request.FILES.get('file')

        # make temp directory
        temp_dir = os.path.join(FileUploadView.temp_base, identifier)
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir, 0o777)

        # save chunk data
        chunk_name = get_chunk_name(filename, chunk_number)
        chunk_file = os.path.join(temp_dir, chunk_name)

        with open(chunk_file, "wb") as file:
            for chunk in chunk_data.chunks():
                file.write(chunk)

        return OkResponse(data={"ok?": "ok"})
