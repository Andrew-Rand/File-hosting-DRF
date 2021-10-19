import os
from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.basecore.responses import OkResponse


class SingleUploadView(generics.GenericAPIView):

    temp_base = os.path.expanduser('home/tmp/uploads')

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:

        file_name = request.data.get('Filename')
        file_data = request.FILES.get('file')

        # make directory
        temp_dir = os.path.join(SingleUploadView.temp_base, file_name)
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir, 0o777)

        saved_file = os.path.join(SingleUploadView.temp_base, file_data)

        with open(saved_file, "wb") as file:
            for row in file_data.chunks():
                file.write(row)

        return OkResponse(data={"ok?": "ok"})
