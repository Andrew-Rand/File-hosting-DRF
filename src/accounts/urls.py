from django.urls import path, include

from .views.login_view import LoginView
from .views.register_view import RegisterView

urlpatterns = [
    path('users', RegisterView.as_view()),
    path('users/login', LoginView.as_view())
]
