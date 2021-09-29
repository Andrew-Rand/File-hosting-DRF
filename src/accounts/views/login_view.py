import datetime

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
import jwt

from src.accounts.models import User
from src.accounts.serializers import UserLoginSerializer
from src.config.settings import SECRET_KEY


class LoginView(generics.GenericAPIView):

    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # email = serializer.data['email']
        # password = serializer.data['password']
        #
        # user = User.objects.filter(email=email).first()
        #
        # if user is None:
        #     raise AuthenticationFailed("User not found!Please check your data and try again. We believe in you!")
        #
        # if not user.password == password:
        #     raise AuthenticationFailed("Incorrect password. Police will be soon!")

        # user authenticated and needs tokens!

        # create access token
        access_token_payload = {
            'id': serializer.data.get('id'),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.utcnow()
        }
        access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm='HS256')

        # create refresh token
        refresh_token_payload = {
            'id': serializer.data.get('id'),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
            'iat': datetime.datetime.utcnow()
        }
        refresh_token = jwt.encode(refresh_token_payload, SECRET_KEY, algorithm='HS256')

        #  add tokens to response
        response = Response()
        response.set_cookie(key='refresh-token', value=refresh_token, httponly=True)
        response.data = {
            'access-token': access_token,
            'user': serializer.data.get('id')
        }
        return response
