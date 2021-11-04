from django.urls import re_path

from .views.all_files_download_view import AllFilesDownloadView
from .views.file_build_view import FileBuildView
from .views.chunk_upload_view import ChunkUploadView
from .views.file_download_view import FileDownloadView
from .views.file_upload_view import FileUploadView
from .views.upload_template_view import UploadTemplateView

urlpatterns = [
    re_path(r'^template/$', UploadTemplateView.as_view(), name='api_file_upload'),
    re_path(r'^chunk-upload/$', ChunkUploadView.as_view(), name='chunk_upload'),
    re_path(r'^build/$', FileBuildView.as_view(), name='file_build'),
    re_path(r'^file-upload/$', FileUploadView.as_view(), name='file_upload'),
    re_path(r'^(?P<pk>[0-9A-Fa-f-]+)/download$', FileDownloadView.as_view(), name='file_download'),
    re_path(r'^download/$', AllFilesDownloadView.as_view(), name='all_download_zip'),
]
