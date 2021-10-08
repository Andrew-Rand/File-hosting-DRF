from typing import Dict, Any

from rest_framework import serializers
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'username')
        extra_kwargs = {
            'password': {'write_only': True}  # hide password in response
        }

    def create(self, validated_data: Dict[str, Any]) -> User:
        user = User.objects.create_user(**validated_data)

        return user
