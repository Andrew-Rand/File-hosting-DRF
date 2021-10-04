from django.contrib.auth import authenticate
from rest_framework import serializers
from .models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # hide password in response
        }


class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')

    def validate(self, data: dict) -> dict:
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(f"User with {email} and {password} not found")
        return {
            "id": user.id,
            "email": user.email
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
