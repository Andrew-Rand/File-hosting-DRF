from django.urls import path, include

from .views.login_view import LoginView
from .views.register_view import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view())
]
