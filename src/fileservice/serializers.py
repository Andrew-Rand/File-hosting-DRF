from rest_framework import serializers

from src.fileservice.models.File import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'title', 'file', 'date_created')