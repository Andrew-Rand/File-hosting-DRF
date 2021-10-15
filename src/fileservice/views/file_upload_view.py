import os
from typing import Any

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.request import Request

from src.basecore.custom_error_handler import BadRequestError, NotFoundError
from src.basecore.responses import OkResponse


def get_chunk_name(uploaded_filename: str, chunk_number: int) -> str:
    return uploaded_filename + f"_part_{chunk_number}"


class FileUploadView(generics.GenericAPIView):

    TempBase = os.path.expanduser("home/tmp/uploads")

    def get(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse:
        resumable_identifier = request.query_params.get('resumableIdentifier')
        resumable_filename = request.query_params.get('resumableFilename')
        resumable_chunk_number = int(request.query_params.get('resumableChunkNumber'))

        if not resumable_identifier or not resumable_filename or not resumable_chunk_number:
            # Parameters are missing or invalid
            # BadRequestError('Parameter error')
            return HttpResponse(400, "parameter error")

        temp_dir = os.path.join(FileUploadView.TempBase, resumable_identifier)

        chunk_file = os.path.join(temp_dir, get_chunk_name(resumable_filename, resumable_chunk_number))
        print(f'Get chunk: {chunk_file}')

        if os.path.isfile(chunk_file):
            return OkResponse({"ok":"Ok"})
        else:
            # Let resumable.js know this chunk does not exists and needs to be uploaded
            return NotFoundError()


    def post(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponse:
        resumable_total_chunks = int(request.data.get('resumableTotalChunks'))
        resumable_chunk_number = int(request.data.get('resumableChunkNumber'))
        resumable_filename = request.data.get('resumableFilename')
        resumable_identifier = request.data.get('resumableIdentifier')

        # get chunk data
        chunk_data = request.FILES.get('file')

        # make temp directory
        temp_dir = os.path.join(FileUploadView.TempBase, resumable_identifier)
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir, 0o777)

        # save chunk data
        chunk_name = get_chunk_name(resumable_filename, resumable_chunk_number)
        chunk_file = os.path.join(temp_dir, chunk_name)

        with open(chunk_file, "wb") as file:
            for chunk in chunk_data.chunks():
                file.write(chunk)

        print(f'Saved chunk: {chunk_file}')

        # check if the upload is complete
        chunk_paths = [os.path.join(temp_dir, get_chunk_name(resumable_filename, x)) for x in
                       range(1, resumable_total_chunks + 1)]
        upload_complete = all([os.path.exists(p) for p in chunk_paths])

        # create final file from all chunks
        if upload_complete:
            target_file_name = os.path.join(FileUploadView.TempBase, resumable_filename)
            with open(target_file_name, "ab") as target_file:
                for p in chunk_paths:
                    stored_chunk_file_name = p
                    stored_chunk_file = open(stored_chunk_file_name, 'rb')
                    target_file.write(stored_chunk_file.read())
                    stored_chunk_file.close()
                    os.unlink(stored_chunk_file_name)
            target_file.close()
            os.rmdir(temp_dir)
            print(f'File saved to: {target_file_name}')

        return HttpResponse(200, "File saved to: {target_file}")
