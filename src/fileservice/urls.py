from django.urls import path

from src.fileservice.views.all_files_view import AllFilesView
from src.fileservice.views.download_file import DownloadFile
from src.fileservice.views.file_view import FileView

urlpatterns = [
    path('upload', FileView.as_view(), name="upload"),
    path('', AllFilesView.as_view(), name="index"),
    path('download', DownloadFile.as_view(), name="download")
]
