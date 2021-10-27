import os
from typing import Any

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.responses import OkResponse
from src.fileservice.models import FileStorage, File
from src.fileservice.models.file_storage import PERMANENT_STORAGE
from src.fileservice.serializers.file_upload_parameters_serializer import FileUploadParametersSerializer
from src.fileservice.utils import calculate_hash_md5


class FileUploadView(generics.GenericAPIView):

    permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)
    serializer_class = FileUploadParametersSerializer

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        filename = serializer.validated_data.get('filename')
        file_data = request.FILES.get('file')

        # make directory
        user_dir_path = os.path.join(self.permanent_storage.destination, str(user.id))
        file_dir_path = os.path.join(user_dir_path, filename)
        os.makedirs(file_dir_path, 0o777, exist_ok=True)

        file_path = os.path.join(file_dir_path, filename)

        with open(file_path, "wb") as file:
            for row in file_data.chunks():
                file.write(row)

        file_hash = calculate_hash_md5(file_path)

        File.create_model_object(user, file_hash, self.permanent_storage, file_path, serializer.validated_data)

        return OkResponse({})
