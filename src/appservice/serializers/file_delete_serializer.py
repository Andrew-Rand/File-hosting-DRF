from rest_framework import serializers

from src.fileservice.models import File


class FileDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('is_alive', )
