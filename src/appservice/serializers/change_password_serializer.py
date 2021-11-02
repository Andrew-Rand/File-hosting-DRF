from rest_framework import serializers

from src.accounts.models import User


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('password', 'new_password', )
