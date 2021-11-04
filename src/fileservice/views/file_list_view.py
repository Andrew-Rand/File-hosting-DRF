from typing import Any

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.responses import OkResponse
from src.fileservice.serializers.file_serializer import FileSerializer
from src.fileservice.models import File
from src.fileservice.utils import PaginationFiles
from src.fileservice.views.constants import ORDERING_FILED


class FileListView(generics.GenericAPIView):

    pagination_class = PaginationFiles
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ORDERING_FILED

    # @login_required
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = User.objects.get(id='ca1890fe-c030-468c-9a87-964a218f13b2')
        queryset = File.objects.filter(user=user)
        serializer = FileSerializer(instance=queryset, many=True)

        return OkResponse(self.paginate_queryset(serializer.data))
