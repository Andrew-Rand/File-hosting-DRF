from django.urls import path

from .views.RaiseView import RaiseView
from .views.auth_view import AuthView
from .views.login_view import LoginView
from .views.refresh_view import RefreshView
from .views.register_view import RegisterView

urlpatterns = [
    path('/', AuthView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', RefreshView.as_view()),
    path('raise/', RaiseView.as_view()),
]
