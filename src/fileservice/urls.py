from django.urls import re_path

from .views.file_upload_view import FileUploadView
from .views.api_upload import ApiUploadView

urlpatterns = [
    re_path(r'^api/upload/$', ApiUploadView.as_view(), name="api_file_upload"),
    re_path(r'^upload/$', FileUploadView.as_view(), name="file_upload"),
]
