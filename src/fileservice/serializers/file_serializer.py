from rest_framework import serializers

from src.fileservice.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'name', 'type', 'date_created', 'date_modified', 'is_alive', 'description')
