from django.contrib.auth.models import User
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = "fullName", "email", "phone", "avatar"

    fullName = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    # noinspection PyPep8Naming
    # noinspection PyMethodMayBeStatic
    def get_fullName(self, obj: User):
        return obj.username

    # noinspection PyMethodMayBeStatic
    def get_phone(self, obj: User):
        return obj.profile.phone

    # noinspection PyMethodMayBeStatic
    def get_avatar(self, obj: User):
        return {"src": obj.avatar.image.path, "alt": obj.avatar.alt}
