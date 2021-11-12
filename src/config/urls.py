from decouple import config
from django.contrib import admin
from django.urls import path, include

from src.config.settings import APP_TYPE

urlpatterns = [
    path('admin/', admin.site.urls)
]

if APP_TYPE == config('AUTH_ENVIRONMENT'):
    urlpatterns = [
        path('api/accounts/', include('src.accounts.urls')),
    ]

elif APP_TYPE == config('FILE_ENVIRONMENT'):
    urlpatterns = [
        path('api/files/', include('src.fileservice.urls')),
    ]
