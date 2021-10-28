from rest_framework import serializers

from src.fileservice.models import File


class FileSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField()

    class Meta:
        model = File
        fields = ('id', 'name')
