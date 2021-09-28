import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings

from .models.user import User


class JWTAuth(BaseAuthentication):

    def authenticate(self, request):

        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            return None

        try:
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('This user does not exist')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User was deactivated')

        return user, None
