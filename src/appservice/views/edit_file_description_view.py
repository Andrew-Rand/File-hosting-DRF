from typing import Any

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.authentication import login_required
from src.accounts.models import User
from src.basecore.custom_error_handler import NotFoundError, ForbiddenError
from src.basecore.responses import OkResponse
from src.fileservice.models import File


class EditFiledescriptionView(generics.GenericAPIView):

    @login_required
    def put(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        try:
            file = File.objects.get(id=self.kwargs['pk'])
        except File.DoesNotExist:
            raise NotFoundError('This file does not exist')
        if not file.user == user:
            raise ForbiddenError('This file doesn`t belong to you')
        file.description = request.data.get('description ')
        file.save()
        return OkResponse({})
