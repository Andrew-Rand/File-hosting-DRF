from django.urls import re_path, path

from .views.file_list_view import FileListView
from .views.file_build_view import FileBuildView
from .views.chunk_upload_view import ChunkUploadView
from .views.file_view import FileView
from .views.file_upload_view import FileUploadView
from .views.upload_template_view import UploadTemplateView


urlpatterns = [
    re_path(r'^template/$', UploadTemplateView.as_view(), name='api_file_upload'),
    re_path(r'^chunk-upload/$', ChunkUploadView.as_view(), name='chunk_upload'),
    re_path(r'^build/$', FileBuildView.as_view(), name='file_build'),
    re_path(r'^file-upload/$', FileUploadView.as_view(), name='file_upload'),
    re_path(r'^/$', FileListView.as_view(), name='files'),
    path('<uuid:pk>/', FileView.as_view(), name='file'),
]
