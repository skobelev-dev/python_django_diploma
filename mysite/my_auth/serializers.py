from rest_framework import serializers

from media.serializers import AvatarSerializer


class ProfileSerializer(serializers.Serializer):
    fullName = serializers.CharField(max_length=100)
    email = serializers.EmailField(allow_blank=True)
    phone = serializers.CharField(max_length=20, required=False)
    avatar = AvatarSerializer()
