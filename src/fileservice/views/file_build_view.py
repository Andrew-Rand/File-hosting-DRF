import os
from typing import Any

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.responses import OkResponse
from src.fileservice.models.file_storage import TEMP_STORAGE, PERMANENT_STORAGE
from src.fileservice.utils import get_chunk_name, is_all_chunk_uploaded
from src.fileservice.models import FileStorage
from src.fileservice.serializers.file_upload_parameters_serializer import FileUploadParametersSerializer
from src.fileservice.tasks import task_build_file


class FileBuildView(generics.GenericAPIView):

    temp_storage = FileStorage.objects.get(type=TEMP_STORAGE)
    permanent_storage = FileStorage.objects.get(type=PERMANENT_STORAGE)
    serializer_class = FileUploadParametersSerializer

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:

        serializer = self.get_serializer(data=request.query_params)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        identifier = serializer.validated_data.get('identifier')
        filename = serializer.validated_data.get('filename')
        total_chunks = serializer.validated_data.get('total_chunk')

        user_dir_path = os.path.join(self.temp_storage.destination, str(user.id))
        chunks_dir_path = os.path.join(user_dir_path, identifier)

        #  save file from chunks with celery

        chunk_paths = [
            os.path.join(chunks_dir_path, get_chunk_name(filename, x))
            for x in range(1, total_chunks + 1)
        ]
        if is_all_chunk_uploaded(chunk_paths):
            task_build_file.delay(user_id=user.id,
                                  temp_storagese_id=self.temp_storage.id,
                                  permanent_storage_id=self.permanent_storage.id,
                                  data=serializer.validated_data)

        return OkResponse(data=serializer.data)
