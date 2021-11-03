from django.urls import re_path

from .views.change_password_view import ChangePasswordView
from .views.login_view import LoginView
from .views.refresh_view import RefreshView
from .views.register_view import RegisterView
from .views.user_detail_view import UserDetailView

urlpatterns = [
    re_path(r'^register/$', RegisterView.as_view(), name="register"),
    re_path(r'^login/$', LoginView.as_view(), name="login"),
    re_path(r'^refresh/$', RefreshView.as_view(), name="refresh"),
    re_path(r'^/$', UserDetailView.as_view(), name='user_view_and_update'),
    re_path(r'^change_password/$', ChangePasswordView.as_view(), name='change_password'),
]
