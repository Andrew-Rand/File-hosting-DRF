from django.urls import re_path

from .views.all_files_view import AllFilesView


urlpatterns = [
    re_path(r'^files/$', AllFilesView.as_view(), name='all_user_files'),
]
