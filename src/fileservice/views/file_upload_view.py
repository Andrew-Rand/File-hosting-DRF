import os
from typing import Any

from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from src.basecore.custom_error_handler import BadRequestError, NotFoundError
from src.basecore.responses import OkResponse


def get_chunk_name(uploaded_filename, chunk_number):
    return uploaded_filename + "_part_%03d" % chunk_number


class FileUploadView(generics.GenericAPIView):

    TempBase = os.path.expanduser("home/tmp/uploads")

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        resumable_identfier = request.data.get('resumableIdentifier', type=str)
        resumable_filename = request.data.get('resumableFilename', type=str)
        resumable_chunk_number = request.data.get('resumableChunkNumber', type=int)

        if not resumable_identfier or not resumable_filename or not resumable_chunk_number:
            # Parameters are missing or invalid
            BadRequestError('Parameter error')

        # chunk folder path based on the parameters
        temp_dir = os.path.join(FileUploadView.TempBase, resumable_identfier)

        # chunk path based on the parameters
        chunk_file = os.path.join(temp_dir, get_chunk_name(resumable_filename, resumable_chunk_number))
        print(f'Getting chunk: {chunk_file}')

        if os.path.isfile(chunk_file):
            # Let resumable.js know this chunk already exists
            response_data = {"File upload": "Yes"}
            return OkResponse(data=response_data)
        else:
            # Let resumable.js know this chunk does not exists and needs to be uploaded
            raise NotFoundError('Not found')


    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        resumable_total_chunks = request.form.get('resumableTotalChunks', type=int)
        resumable_chunk_number = request.form.get('resumableChunkNumber', default=1, type=int)
        resumable_filename = request.form.get('resumableFilename', default='error', type=str)
        resumable_identfier = request.form.get('resumableIdentifier', default='error', type=str)

        # get the chunk data
        chunk_data = request.files['file']

        # make our temp directory
        temp_dir = os.path.join(FileUploadView.TempBase, resumable_identfier)
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir, 0o777)

        # save the chunk data
        chunk_name = get_chunk_name(resumable_filename, resumable_chunk_number)
        chunk_file = os.path.join(temp_dir, chunk_name)
        chunk_data.save(chunk_file)
        print(f'Saved chunk: {chunk_file}')

        # check if the upload is complete
        chunk_paths = [os.path.join(temp_dir, get_chunk_name(resumable_filename, x)) for x in
                       range(1, resumable_total_chunks + 1)]
        upload_complete = all([os.path.exists(p) for p in chunk_paths])

        # combine all the chunks to create the final file
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

        response_data = {"File saved to": target_file}
        return OkResponse(data=response_data)
