from django.urls import path, include

from .views.login_view import LoginView
from .views.profile_view import ProfileView
from .views.register_view import RegisterView

urlpatterns = [
    path('users', ProfileView.as_view()),
    path('users/register', RegisterView.as_view()),
    path('users/login', LoginView.as_view())
]
