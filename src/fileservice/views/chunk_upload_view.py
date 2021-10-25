import os
from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.basecore.custom_error_handler import BadRequestError, NotFoundError
from src.basecore.responses import OkResponse


def get_chunk_name(uploaded_filename: str, chunk_number: int) -> str:
    return f'{uploaded_filename}_part_{chunk_number}'


class FileUploadView(generics.GenericAPIView):

    TempBase = os.path.expanduser("home/tmp/uploads")

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        identifier = request.query_params.get('resumableIdentifier')
        filename = request.query_params.get('resumableFilename')
        chunk_number = int(request.query_params.get('resumableChunkNumber'))

        if not identifier or not filename or not chunk_number:
            # Parameters are missing or invalid
            raise BadRequestError()

        temp_dir = os.path.join(FileUploadView.TempBase, identifier)

        chunk_file = os.path.join(temp_dir, get_chunk_name(filename, chunk_number))

        if os.path.isfile(chunk_file):
            return OkResponse(data={"ok?": "ok"})
        else:
            # Let resumable.js know this chunk does not exists and needs to be uploaded
            raise NotFoundError()

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        chunk_number = int(request.data.get('resumableChunkNumber'))
        filename = request.data.get('resumableFilename')
        identifier = request.data.get('resumableIdentifier')

        # get chunk data
        chunk_data = request.FILES.get('file')

        # make temp directory
        temp_dir = os.path.join(FileUploadView.TempBase, identifier)
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir, 0o777)

        # save chunk data
        chunk_name = get_chunk_name(filename, chunk_number)
        chunk_file = os.path.join(temp_dir, chunk_name)

        with open(chunk_file, "wb") as file:
            for chunk in chunk_data.chunks():
                file.write(chunk)

        return OkResponse(data={"ok?": "ok"})
