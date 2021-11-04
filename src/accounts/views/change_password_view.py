from typing import Any

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.accounts.serializers.change_password_serializer import ChangePasswordSerializer
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
        if not user.check_password(password):
            raise BadRequestError({'incorrect password'})
        user.set_password(serializer.validated_data.get('new_password'))
        user.save()
        return CreatedResponse({})
