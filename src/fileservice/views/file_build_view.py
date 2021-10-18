import os
from typing import Any, List

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.basecore.responses import OkResponse
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

    TempBase = os.path.expanduser("home/tmp/uploads")

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        total_chunks = int(request.data.get('resumableTotalChunks'))
        filename = request.data.get('resumableFilename')
        identifier = request.data.get('resumableIdentifier')

        # make temp directory
        temp_dir = os.path.join(FileBuildView.TempBase, identifier)

        # check if the upload is complete
        chunk_paths = [os.path.join(temp_dir, get_chunk_name(filename, x)) for x in
                       range(1, total_chunks + 1)]
        upload_complete = all([os.path.exists(p) for p in chunk_paths])

        # create final file from all chunks
        if upload_complete:
            target_file_name = os.path.join(FileBuildView.TempBase, filename)
            build_file(target_file_name, chunk_paths)
            os.rmdir(temp_dir)

        return OkResponse(data={"ok?": "ok"})
