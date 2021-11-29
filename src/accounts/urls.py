from django.urls import re_path

from .constants import ACCOUNTS_REGISTER_URL_NAME, ACCOUNTS_LOGIN_URL_NAME, ACCOUNTS_REFRESH_URL_NAME, \
    ACCOUNTS_DETAIL_URL_NAME, ACCOUNTS_CHANGE_PASSWORD_URL_NAME
from .views.change_password_view import ChangePasswordView
from .views.login_view import LoginView
from .views.refresh_view import RefreshView
from .views.register_view import RegisterView
from .views.user_detail_view import UserDetailView

urlpatterns = [
    re_path(r'^register/$', RegisterView.as_view(), name=ACCOUNTS_REGISTER_URL_NAME),
    re_path(r'^login/$', LoginView.as_view(), name=ACCOUNTS_LOGIN_URL_NAME),
    re_path(r'^refresh/$', RefreshView.as_view(), name=ACCOUNTS_REFRESH_URL_NAME),
    re_path(r'^profile/$', UserDetailView.as_view(), name=ACCOUNTS_DETAIL_URL_NAME),
    re_path(r'^change_password/$', ChangePasswordView.as_view(), name=ACCOUNTS_CHANGE_PASSWORD_URL_NAME),
]
