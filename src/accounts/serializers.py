from typing import Dict, Any

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

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None:
            raise serializers.ValidationError(f"User with username: {username} and password: {password} not found")
        print(user.password, password)
        if user.password == password:
            return {
                "id": user.id,
                "email": user.email
            }
        else:
            raise serializers.ValidationError("Incorrect password")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
