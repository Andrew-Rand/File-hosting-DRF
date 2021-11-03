import os
from typing import Any

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.custom_error_handler import BadRequestError, NotFoundError
from src.basecore.responses import OkResponse
from src.fileservice.models import File


class FileDownloadView(generics.GenericAPIView):

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        try:
            file = File.objects.get(id=self.kwargs['pk'])
        except File.DoesNotExist:
            raise NotFoundError('This file does not exist')

        if not file.user.id == user.id:
            raise BadRequestError('This user doesn`t  have this file in own repository')

        file_path = file.get_absolute_path()

        if not os.path.exists(file_path):
            raise NotFoundError('file doesn`t exist in storrage')

        return Response(content_type='application/force-download',
                        headers={'Content-Disposition': f'attachment; filename="{file.name}"',
                                 'X-Accel-Redirect': file.get_absolute_path})
