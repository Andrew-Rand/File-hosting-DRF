from django.urls import re_path

from .views.auth_view import AuthView
from .views.login_view import LoginView
from .views.refresh_view import RefreshView
from .views.register_view import RegisterView

urlpatterns = [
    re_path(r'^/$', AuthView.as_view(), name="test_login"),
    re_path(r'^register/$', RegisterView.as_view(), name="register"),
    re_path(r'^login/$', LoginView.as_view(), name="login"),
    re_path(r'^refresh/$', RefreshView.as_view(), name="refresh"),
]
