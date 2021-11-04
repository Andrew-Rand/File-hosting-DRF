from typing import Any
from uuid import UUID

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.custom_error_handler import NotFoundError
from src.fileservice.models import File


class FileDownloadView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, pk: UUID, *args: Any, user: User, **kwargs: Any) -> Response:

        if not File.objects.filter(id=pk, user=user).exists():
            raise NotFoundError('This file does not exist')

        file = File.objects.get(id=self.kwargs['pk'])

        file_path = file.absolute_path

        return Response(content_type='application/force-download',
                        headers={'Content-Disposition': f'attachment; filename="{file.name}"',
                                 'X-Accel-Redirect': file_path})
