from django.urls import re_path

from .views.all_files_view import AllFilesView
from .views.delete_file_view import DeleteFileView
from .views.file_detail_view import FileDetailView

urlpatterns = [
    re_path(r'^files/$', AllFilesView.as_view(), name='all_user_files'),
    re_path(r'^files/(?P<pk>.+)/$', FileDetailView.as_view(), name='file_detail'),
    re_path(r'delete/(?P<pk>.+)/$', DeleteFileView.as_view(), name='delete_file')
]
