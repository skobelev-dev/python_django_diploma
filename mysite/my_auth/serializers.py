from django.contrib.auth.models import User
from django.db.models import QuerySet
from rest_framework import serializers

import mysite.settings
from my_auth.models import Profile

class AvatarSerializer(serializers.Serializer):
    src = serializers.FilePathField(path=mysite.settings.MEDIA_ROOT, allow_blank=True, allow_null=True)
    alt = serializers.CharField(allow_blank=True)

class MyProfileSerializer(serializers.Serializer):
    fullName = serializers.CharField(max_length=100)
    email = serializers.EmailField(allow_blank=True)
    phone = serializers.CharField(max_length=20, required=False)
    avatar = AvatarSerializer()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = 'fullName', 'email', 'phone', 'avatar'

    fullName = serializers.CharField(source="user.username")
    email = serializers.EmailField(source="user.email")
    avatar = AvatarSerializer()