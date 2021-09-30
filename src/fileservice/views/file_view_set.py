from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.fileservice.models.File import File
from src.fileservice.serializers import FileSerializer


class UploadViewSet(ViewSet):
    serializer_class = FileSerializer
    permission_classes = [AllowAny, ]

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)