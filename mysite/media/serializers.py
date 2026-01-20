from rest_framework import serializers


class AvatarSerializer(serializers.Serializer):
    src = serializers.CharField(max_length=200, allow_blank=True)
    alt = serializers.CharField(allow_blank=True)
