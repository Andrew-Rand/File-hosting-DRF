from django.urls import re_path

from .views.file_upload_view import FileUploadView
from .views.upload_template_view import UploadTemplateView

urlpatterns = [
    re_path(r'^template/$', UploadTemplateView.as_view(), name="api_file_upload"),
    re_path(r'^upload/$', FileUploadView.as_view(), name="file_upload"),
]
