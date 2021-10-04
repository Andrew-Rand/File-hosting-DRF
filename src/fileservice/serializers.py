from typing import Any

from rest_framework import serializers

from src.fileservice.models.File import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('id', 'owner', 'title', 'file', 'date_created')

    def create(self, validated_data: Any) -> object:
        return File.objects.create(**validated_data)
