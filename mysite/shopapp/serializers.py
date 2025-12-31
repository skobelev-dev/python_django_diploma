from rest_framework import serializers
import pytz

from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "id", "category", "price", "date", "title", 'description',

    id = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    # noinspection PyMethodMayBeStatic
    def get_id(self , obj: Product):
        return f"{obj.pk}"

    # noinspection PyMethodMayBeStatic
    def get_date(self, obj):
        cet_tz = pytz.timezone("Europe/Paris")  # или 'Europe/Berlin'
        localized = obj.date.astimezone(cet_tz)


        time_str = localized.strftime("%a %b %d %Y %H:%M:%S GMT%z")
        tz_name = cet_tz.tzname(localized)

        return f"{time_str} ({tz_name})"
