from rest_framework import serializers


class UploadDataSerializer(serializers.Serializer):
    resumable_total_chunks = serializers.IntegerField(required=True, min_value=1)
    resumable_chunk_number = serializers.IntegerField(required=True, min_value=1)
    resumable_filename = serializers.CharField(max_length=256, required=True)
    resumable_identifier = serializers.CharField(max_length=256, required=True)
