from reviews.models import Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "author", "email", "text", "rate", "date"

    author = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    # noinspection PyMethodMayBeStatic
    def get_author(self, obj: Review):
        author = obj.author.username
        return author

    # noinspection PyMethodMayBeStatic
    def get_email(self, obj: Review):
        email = obj.author.email
        return email
