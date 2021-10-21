from django.urls import re_path

from .views.file_build_view import FileBuildView
from .views.chunk_upload_view import ChunkUploadView
from .views.upload_template_view import UploadTemplateView

urlpatterns = [
    re_path(r'^template/$', UploadTemplateView.as_view(), name='api_file_upload'),
    re_path(r'^upload/$', ChunkUploadView.as_view(), name='file_upload'),
    re_path(r'^build/$', FileBuildView.as_view(), name='file_build')
]
