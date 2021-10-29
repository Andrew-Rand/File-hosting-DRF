from typing import Any

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.responses import OkResponse
from src.fileservice.models.file_storage import TEMP_STORAGE, PERMANENT_STORAGE
from src.fileservice.utils import is_all_chunk_uploaded, make_chunk_paths, make_chunk_dir_path
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

        chunks_dir_path = make_chunk_dir_path(self.temp_storage.destination, str(user.id), serializer.validated_data)

        #  save file from chunks with celery
        chunk_paths = make_chunk_paths(chunks_dir_path, serializer.validated_data)
        print(f'path when build chunks before celery{chunks_dir_path}')
        if is_all_chunk_uploaded(chunk_paths):
            task_build_file.delay(user_id=user.id,
                                  temp_storage_id=self.temp_storage.id,
                                  permanent_storage_id=self.permanent_storage.id,
                                  data=serializer.validated_data)

        return OkResponse(data=serializer.data)
