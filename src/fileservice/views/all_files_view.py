from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from src.fileservice.models.File import File
from src.fileservice.serializers import FileSerializer


class AllFilesView(generics.GenericAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny, ]

    def get(self, request):
        # get all the data from table Files
        queryset = File.objects.all()
        # serialize this data
        serialized_queryset = FileSerializer(instance=queryset, many=True)
        return Response(serialized_queryset.data)
