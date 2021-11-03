from django.urls import re_path

from .views.all_files_view import AllFilesView
from .views.file_build_view import FileBuildView
from .views.chunk_upload_view import ChunkUploadView
from .views.file_delete_view import DeleteFileView
from .views.file_detail_view import FileDetailView
from .views.file_edit_description_view import EditFiledescriptionView
from .views.file_upload_view import FileUploadView
from .views.upload_template_view import UploadTemplateView


urlpatterns = [
    re_path(r'^template/$', UploadTemplateView.as_view(), name='api_file_upload'),
    re_path(r'^chunk-upload/$', ChunkUploadView.as_view(), name='chunk_upload'),
    re_path(r'^build/$', FileBuildView.as_view(), name='file_build'),
    re_path(r'^file-upload/$', FileUploadView.as_view(), name='file_upload'),
    re_path(r'^/$', AllFilesView.as_view(), name='all_user_files'),
    re_path(r'^(?P<pk>[0-9A-Fa-f-]+)/$', FileDetailView.as_view(), name='file_detail'),
    re_path(r'^(?P<pk>[0-9A-Fa-f-]+)/delete/$', DeleteFileView.as_view(), name='delete_file'),
    re_path(r'^(?P<pk>[0-9A-Fa-f-]+)/edit/$', EditFiledescriptionView.as_view(), name='edit_description'),
]
