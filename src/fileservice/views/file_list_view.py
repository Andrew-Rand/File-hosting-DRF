from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.fileservice.serializers.file_serializer import FileSerializer
from src.fileservice.models import File
from src.fileservice.views.constants import PAGINATION_NUMBER, ORDERING_FILED


class FileListView(generics.GenericAPIView):

    paginate_by = PAGINATION_NUMBER
    ordering = ORDERING_FILED

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        queryset = File.objects.filter(user=user)
        serializer = FileSerializer(instance=queryset, many=True)
        return Response(serializer.data)
