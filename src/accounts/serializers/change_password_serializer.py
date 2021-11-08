from typing import Dict, Any

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100)
    new_password_repeated = serializers.CharField(max_length=100)

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:

        user = self.context.get('user')
        if not user:
            raise ValidationError('User not found')
        password = data.get('password')
        new_password = data.get('new_password')
        new_password_repeated = data.get('new_password_repeated')

        if not user.check_password(password):
            raise ValidationError({'incorrect password'})
        if new_password != new_password_repeated:
            raise ValidationError({'new passwords do not match'})
        return data

    def set_password(self) -> None:
        user = self.context.get('user')
        user.set_password(self.validated_data.get('new_password'))
        user.save()
