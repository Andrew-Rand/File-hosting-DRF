from django.urls import path, include
from .views.register_view import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view())
]
