from typing import Any

from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.fileservice.models import File
from src.fileservice.serializers.file_serializer import FileSerializer


class FileDownloadView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = FileSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        file_id = serializer.data.get('id')
        queryset = File.objects.filter(id=file_id).first
        print(queryset)

        file_location = queryset.destination

        try:
            with open(file_location, 'r') as f:
                file_data = f.read()

            # sending response
            response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="foo.xls" '
        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound('<h1>File not exist</h1>')
