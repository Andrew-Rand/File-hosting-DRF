from typing import Any

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.responses import OkResponse
from src.fileservice.pagination import FilesPagination
from src.fileservice.serializers.file_serializer import FileSerializer
from src.fileservice.models import File
from src.fileservice.views.constants import ORDERING_FILED


class FileListView(generics.GenericAPIView):

    pagination_class = FilesPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ORDERING_FILED

    # @login_required
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = User.objects.get(id='9148d1e1-5ba3-47e0-84b5-65c157f62e3a')
        queryset = File.objects.filter(user=user)
        serializer = FileSerializer(instance=queryset, many=True)

        return OkResponse(self.paginate_queryset(serializer.data))
