from typing import Dict, Any

from django.contrib.auth import authenticate
from rest_framework import serializers
from .models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'username']
        extra_kwargs = {
            'password': {'write_only': True}  # hide password in response
        }


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(f"User not found")
        return {
            "id": user.id,
            "email": user.email
            }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
