from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed

from src.accounts.models import User


class LoginView(generics.GenericAPIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!Please check your data and try again. We believe in you!")

        if not user.password == password:
            raise AuthenticationFailed("Incorrect password. Police will be soon!")

        return Response({"message": "success"})
