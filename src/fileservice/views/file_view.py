from typing import Any

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

# from src.fileservice.models.File import File
from src.fileservice.models.File import File
from src.fileservice.serializers import FileSerializer


class FileView(generics.GenericAPIView):

    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny, ]

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request) -> Response:
        # queryset = File.objects.filter(title="some_file_4")
        queryset = File.objects.filter(title=request.data.get("title"))
        # serialize this data
        serialized_queryset = FileSerializer(instance=queryset, many=True)
        return Response(serialized_queryset.data)
