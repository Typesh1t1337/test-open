from rest_framework import serializers


class HookSerializer(serializers.Serializer):
    message = serializers.CharField()
    callback = serializers.URLField()

