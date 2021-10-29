import os
import shutil
from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.custom_error_handler import NotFoundError
from src.fileservice.models import FileStorage
from src.fileservice.models.file_storage import PERMANENT_STORAGE


class AllDownloadView(generics.GenericAPIView):

    permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)

    @login_required
    def get(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        archive_type = 'zip'
        user_id = str(user.id)
        user_dir_path = os.path.join(self.permanent_storage.destination, user_id)

        if not os.path.exists(user_dir_path) or len(os.listdir(user_dir_path)) == 0:
            raise NotFoundError('Dir of this user does not exist or empty')

        shutil.make_archive(user_id, archive_type, user_dir_path)

        file_path = os.path.join(user_dir_path, f'{user_id}.{archive_type}')

        return Response(headers={'Content-Disposition': f'attachment; filename="{file_path}"'})
