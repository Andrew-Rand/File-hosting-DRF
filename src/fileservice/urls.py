from django.urls import path, include
from rest_framework import routers

from src.fileservice.views.file_view_set import UploadViewSet

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")


urlpatterns = [
    path('/', include(router.urls)),
]
