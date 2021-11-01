from rest_framework import serializers

from src.fileservice.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('name', 'type', 'date_created')
