from django.contrib import admin
from django.urls import path, include

from src.config.settings import APP_TYPE, APP_TYPE_AUTH, APP_TYPE_FILE, APP_TYPE_TEST

urlpatterns = [
    path('admin/', admin.site.urls)
]

if APP_TYPE == APP_TYPE_AUTH:
    urlpatterns = [
        path('api/accounts/', include('src.accounts.urls')),
    ]

elif APP_TYPE == APP_TYPE_FILE:
    urlpatterns = [
        path('api/files/', include('src.fileservice.urls')),
    ]

elif APP_TYPE == APP_TYPE_TEST:
    urlpatterns = [
        path('api/accounts/', include('src.accounts.urls')),
        path('api/files/', include('src.fileservice.urls')),
    ]
