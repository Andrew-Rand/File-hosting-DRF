from typing import Any

from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.appservice.serializers.change_password_serializer import ChangePasswordSerializer
from src.basecore.custom_error_handler import NotFoundError, BadRequestError
from src.basecore.responses import CreatedResponse


class ChangePasswordView(generics.GenericAPIView):

    @login_required
    def put(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        try:
            user = User.objects.get(id=user.id)
        except User.DoesNotExist:
            raise NotFoundError('This user does not exist')
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        password = serializer.data.get('password')
        user_changed = authenticate(user=user.username, password=password)
        if user_changed is None:
            raise BadRequestError({'incorrect password'})
        user_changed.set_password(serializer.validated_data.get('new_password'))
        return CreatedResponse({})
