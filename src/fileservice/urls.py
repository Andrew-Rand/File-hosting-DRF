from django.urls import path, include

from src.fileservice.views.all_files_view import AllFilesView
from src.fileservice.views.download_file import DownloadFile
from src.fileservice.views.file_view import FileView

urlpatterns = [
    path('upload', FileView.as_view()),
    path('', AllFilesView.as_view()),
    path('download', DownloadFile.as_view())
]
