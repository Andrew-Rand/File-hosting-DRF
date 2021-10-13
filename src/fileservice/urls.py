from django.urls import re_path

from .views.file_upload_view import FileUploadView

urlpatterns = [
    re_path(r'^upload/$', FileUploadView.as_view(), name="file_upload"),
]
