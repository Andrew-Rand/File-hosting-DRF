from typing import Dict, Any

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from src.accounts.models import User


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100)
    new_password_repeated = serializers.CharField(max_length=100)
    id = serializers.UUIDField()

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:

        user = User.objects.get(id=data.get('id'))
        password = data.get('password')
        new_password = data.get('new_password')
        new_password_repeated = data.get('new_password_repeated')

        if not user.check_password(password):
            raise ValidationError({'incorrect password'})
        if new_password != new_password_repeated:
            raise ValidationError({'new passwords do not match'})
        return {
            "new_password": new_password,
        }
