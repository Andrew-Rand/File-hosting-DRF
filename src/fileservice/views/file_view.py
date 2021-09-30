from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from src.fileservice.models.File import File
from src.fileservice.serializers import FileSerializer


class FileView(generics.GenericAPIView):

    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
