from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers import UserSerializer


class ProfileView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user = request.user
        serialized_user = UserSerializer(user).data
        return Response({'user': serialized_user})