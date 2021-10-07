from django.urls import path

from .views.auth_view import AuthView
from .views.login_view import LoginView
from .views.refresh_view import RefreshView
from .views.register_view import RegisterView

urlpatterns = [
    path('/', AuthView.as_view(), name="test_login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('refresh/', RefreshView.as_view(), name="refresh"),
]
