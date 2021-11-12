from typing import Dict, Any

from rest_framework import serializers

from src.accounts.models import User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'age')
        read_only_fields = ('id', 'username', )

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        email = data.get('email')
        if email is None:
            return data
        users_qs = User.objects.filter(email=email).first()

        if users_qs:
            raise serializers.ValidationError("User with this email already exist")

        return data
