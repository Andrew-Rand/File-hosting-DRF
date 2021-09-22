from rest_framework import serializers
from .models.UserProfile import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'name')
