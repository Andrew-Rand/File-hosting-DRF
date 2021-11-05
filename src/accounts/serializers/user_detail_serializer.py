from rest_framework import serializers

from src.accounts.models import User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'age')
        read_only_fields = ('id', 'username', )
