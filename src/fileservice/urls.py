from django.urls import re_path, path

from .constants import FILE_TEMPLATE_URL_NAME, FILE_CHUNK_UPLOAD_URL_NAME, FILE_BUILD_URL_NAME, FILE_UPLOAD_URL_NAME, \
    FILE_DOWNLOAD_URL_NAME, FILE_DOWNLOAD_ALL_URL_NAME, FILE_ALL_USER_FILES_URL_NAME, FILE_DETAIL_URL_NAME
from .views.file_list_view import FileListView
from .views.all_files_download_view import AllFilesDownloadView
from .views.file_build_view import FileBuildView
from .views.chunk_upload_view import ChunkUploadView
from .views.file_view import FileView
from .views.file_download_view import FileDownloadView
from .views.file_upload_view import FileUploadView
from .views.upload_template_view import UploadTemplateView


urlpatterns = [
    re_path(r'^template/$', UploadTemplateView.as_view(), name=FILE_TEMPLATE_URL_NAME),
    re_path(r'^chunk-upload/$', ChunkUploadView.as_view(), name=FILE_CHUNK_UPLOAD_URL_NAME),
    re_path(r'^build/$', FileBuildView.as_view(), name=FILE_BUILD_URL_NAME),
    re_path(r'^file-upload/$', FileUploadView.as_view(), name=FILE_UPLOAD_URL_NAME),
    path('<uuid:pk>/download/', FileDownloadView.as_view(), name=FILE_DOWNLOAD_URL_NAME),
    re_path(r'^download/$', AllFilesDownloadView.as_view(), name=FILE_DOWNLOAD_ALL_URL_NAME),
    re_path(r'^/$', FileListView.as_view(), name=FILE_ALL_USER_FILES_URL_NAME),
    path('<uuid:pk>/', FileView.as_view(), name=FILE_DETAIL_URL_NAME),
]
