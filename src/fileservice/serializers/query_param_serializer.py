from rest_framework import serializers


class QueryParamsSerializer(serializers.Serializer):
    resumable_total_chunks = serializers.IntegerField(required=False)
    resumable_chunk_number = serializers.IntegerField(required=False)
    resumable_filename = serializers.CharField(required=False)
    resumable_identifier = serializers.CharField(required=False)
