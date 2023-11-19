from rest_framework import serializers
from logingestor.models import Log

class LogSerializer(serializers.ModelSerializer):
    metadata = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit', 'metadata']

    def get_metadata(self, obj):
        return {"parentResourceId": obj.parentResourceId}