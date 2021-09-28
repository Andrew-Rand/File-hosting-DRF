import datetime

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
import jwt

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

        # user authenticated and needs token!

        payload = {
            'id': str(user.id),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='JWT', value=token, httponly=True)
        response.data = {
            'JWT': token
        }
        return response
