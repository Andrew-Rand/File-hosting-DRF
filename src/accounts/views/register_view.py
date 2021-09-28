from rest_framework import generics
from rest_framework.response import Response

from ..serializers import UserSerializer


class RegisterView(generics.GenericAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        user = request.user
        serialized_user = UserSerializer(user).data
        return Response({'user': serialized_user})
