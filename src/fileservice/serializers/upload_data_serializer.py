from rest_framework import serializers


class UploadDataSerializer(serializers.Serializer):
    total_chunks = serializers.IntegerField(source='resumableTotalChunks', read_only=True, min_value=1)
    chunk_number = serializers.IntegerField(source='resumableChunkNumber', read_only=True, min_value=1)
    filename = serializers.CharField(source='resumableFilename', max_length=256, read_only=True)
    identifier = serializers.CharField(source='resumableIdentifier', max_length=256, read_only=True)
