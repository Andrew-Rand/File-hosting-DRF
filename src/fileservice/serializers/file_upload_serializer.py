from rest_framework import serializers

from ..models import File


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('user', 'name', 'type', 'storage', 'destination', 'hash', 'size')
