from django.urls import path, include

from src.fileservice.views.file_view import FileView

urlpatterns = [
    path('upload', FileView.as_view()),
]
