import os
from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.custom_error_handler import BadRequestError
from src.basecore.responses import OkResponse
from src.fileservice.models import FileStorage, File
from src.fileservice.models.file_storage import PERMANENT_STORAGE
from src.fileservice.tasks import task_create_tumbnail
from src.fileservice.utils import calculate_hash_md5


class FileUploadView(generics.GenericAPIView):

    permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        file_data = request.FILES.get('file')
        filename = request.data.get('filename')

        # make directory
        user_dir_path = os.path.join(self.permanent_storage.destination, str(user.id))
        os.makedirs(user_dir_path, 0o777, exist_ok=True)

        file_path = os.path.join(user_dir_path, filename)

        with open(file_path, "wb") as file:
            for row in file_data.chunks():
                file.write(row)

        file_hash = calculate_hash_md5(file_path)
        if file_hash != request.data.get('hash'):
            raise BadRequestError('File hash is not match. Try to upload file again')

        relative_path = os.path.join(str(user.id), filename)
        File.create_model_object(user, file_hash, self.permanent_storage, relative_path, request.data)
        task_create_tumbnail.delay(self.permanent_storage.destination + relative_path, request.data.get('type'))

        return OkResponse({})
