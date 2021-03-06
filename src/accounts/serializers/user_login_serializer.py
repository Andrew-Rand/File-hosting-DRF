from typing import Dict, Any

from django.contrib.auth import authenticate
from rest_framework import serializers
from ..models.user import User


class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("User with this username not found or password was incorrect")
        return {
            "id": user.id,
            "username": user.username
        }
