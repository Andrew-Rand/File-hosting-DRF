from django.contrib import admin
from django.urls import path, include

from src.config.settings import APP_TYPE, APP_TYPE_AUTH, APP_TYPE_FILE, APP_TYPE_TEST

urlpatterns = [
    path('admin/', admin.site.urls)
]

user_url = [path('api/accounts/', include('src.accounts.urls')), ]
file_url = [path('api/files/', include('src.fileservice.urls')), ]

if APP_TYPE == APP_TYPE_AUTH:
    urlpatterns = user_url

elif APP_TYPE == APP_TYPE_FILE:
    urlpatterns = file_url

elif APP_TYPE == APP_TYPE_TEST:
    urlpatterns = user_url + file_url
