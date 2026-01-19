from django.contrib.auth.models import User
from django.db.models import QuerySet
from rest_framework import serializers

from my_auth.models import Profile


def get_profile(obj):
    obj_class = obj.__class__
    if obj_class == QuerySet:
        return obj[0]
    return obj


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = "fullName", "email", "phone", "avatar"

    fullName = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    # noinspection PyPep8Naming
    # noinspection PyMethodMayBeStatic
    def get_fullName(self, obj: Profile | QuerySet[Profile]):
        profile = get_profile(obj)
        return profile.user.username

    # noinspection PyMethodMayBeStatic
    def get_phone(self, obj: Profile | QuerySet[Profile]):
        profile = get_profile(obj)
        return str(profile.phone)

    # noinspection PyMethodMayBeStatic
    def get_avatar(self, obj: Profile | QuerySet[Profile]):
        profile = get_profile(obj)
        avatar = profile.user.avatar or None
        image = avatar.image or None
        path = image.path if image else ""
        return {"src": path, "alt": avatar.alt or ""}
