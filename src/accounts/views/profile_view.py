from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import User
from ..serializers import UserSerializer


class ProfileView(generics.GenericAPIView):

    def get(self, request):
        id = request.data['id']
        user = User.objects.filter(id=id).first()
        response = Response()
        response.data = {
            'user': user
        }
