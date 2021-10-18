from rest_framework import serializers


class UploadDataSerializer(serializers.Serializer):
    resumable_total_chunks = serializers.IntegerField(read_only=True, min_value=1)
    resumable_chunk_number = serializers.IntegerField(read_only=True, min_value=1)
    resumable_filename = serializers.CharField(max_length=256, read_only=True)
    resumable_identifier = serializers.CharField(max_length=256, read_only=True)
