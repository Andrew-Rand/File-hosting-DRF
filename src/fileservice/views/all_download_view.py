
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
    def get(self, request: Request, user: User, *args: Any, **kwargs: Any) -> Response:
        archive_type = 'zip'
        user_id = user.id
        user_dir_path = os.path.join(self.permanent_storage.destination, user_id)

        if not os.path.exists(user_dir_path) or len(os.listdir(user_dir_path)) == 0:
            raise NotFoundError('Dir of this user does not exist or empty')

        archive_path = shutil.make_archive(base_name=user_dir_path, format=archive_type, root_dir=self.permanent_storage.destination, base_dir=user_id)
        archive_name = f'{user_id}.zip'

        return Response(content_type='application/force-download',
                        headers={'Content-Disposition': f'attachment; filename={archive_name}',
                                 'X-Accel-Redirect': archive_path})
