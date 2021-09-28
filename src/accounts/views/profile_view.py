from rest_framework import generics
from rest_framework.response import Response

from ..serializers import UserSerializer


class ProfileView(generics.GenericAPIView):

    def get(self, request):
        serializer = UserSerializer(data=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
