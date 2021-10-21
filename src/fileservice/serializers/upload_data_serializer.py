from rest_framework import serializers


class UploadDataSerializer(serializers.Serializer):
    resumableTotalChunks = serializers.IntegerField(min_value=1, required=False)
    resumableChunkNumber = serializers.IntegerField(min_value=1, required=False)
    resumableFilename = serializers.CharField(max_length=256)
    resumableIdentifier = serializers.CharField(max_length=256)
    resumableType = serializers.CharField(max_length=256, required=False)
    resumableTotalSize = serializers.CharField(max_length=256, required=False)
