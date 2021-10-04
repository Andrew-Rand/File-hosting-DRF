import os
import pathlib
import base64

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from src.fileservice.models.File import File
from src.fileservice.serializers import FileSerializer


class DownloadFile(generics.GenericAPIView):
    permission_classes = [AllowAny, ]

    def get(self, request: Request) -> Response:
        queryset = File.objects.filter(title=request.data.get('title')).first()
        serialized_queryset = FileSerializer(instance=queryset)

        dir_path = pathlib.Path.cwd()
        file_path = serialized_queryset.data.get("file")
        path = str(dir_path) + str(file_path)

        if os.path.exists(path):
            with open(path, "rb") as file_to_download:
                file_content = file_to_download.read()
                encoded_file = base64.b64encode(file_content)
                return Response({"encoded_file": encoded_file})
        else:
            return Response({"File does not exist"})
