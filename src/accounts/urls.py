from django.urls import path

from .views.auth_view import AuthView
from .views.login_view import LoginView
from .views.refresh_view import RefreshView
from .views.register_view import RegisterView

urlpatterns = [
    path('/', AuthView.as_view()),
    path('users/register', RegisterView.as_view()),
    path('users/login', LoginView.as_view()),
    path('users/refresh', RefreshView.as_view()),
]
