from rest_framework import serializers


class UploadDataSerializer(serializers.Serializer):
    resumableTotalChunks = serializers.IntegerField(source='total_chunk', min_value=1)
    resumableChunkNumber = serializers.IntegerField(source='chunk_number', min_value=1)
    resumableFilename = serializers.CharField(source='filename', max_length=256)
    resumableIdentifier = serializers.CharField(source='identifier', max_length=256)
    resumableType = serializers.CharField(source='type', max_length=256)
    resumableTotalSize = serializers.CharField(source='total_size', max_length=256)
