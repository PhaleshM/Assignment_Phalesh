from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    metadata = serializers.JSONField(required=False, default={})

    class Meta:
        model = Log
        fields = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit', 'metadata']

    def validate_metadata(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Metadata must be a dictionary.")
        return value
    
    def create(self, validated_data):
        metadata = validated_data.pop('metadata', {})
        validated_data['parentResourceId'] = metadata.get('parentResourceId', None)
        return super(LogSerializer, self).create(validated_data)