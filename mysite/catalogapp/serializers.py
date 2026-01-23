from django_stubs_ext.db.models.manager import ManyRelatedManager
from rest_framework import serializers
import pytz
from rest_framework.decorators import action
from rest_framework.response import Response

from media.models import ProductImage
from reviews.serializers import ReviewSerializer
from .models import Product, Tag, Basket


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "price",
            "date",
            "title",
            "description",
            "fullDescription",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "specifications",
            "rating",
        )

    id = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    fullDescription = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    specifications = serializers.SerializerMethodField()

    # noinspection PyMethodMayBeStatic
    def get_id(self, obj: Product):
        return f"{obj.pk}"

    # noinspection PyMethodMayBeStatic
    def get_date(self, obj: Product):
        cet_tz = pytz.timezone("Europe/Paris")
        if obj.date.tzinfo is None:
            localized = cet_tz.localize(obj.date)
        else:
            localized = obj.date

        time_str = localized.strftime("%a %b %d %Y %H:%M:%S GMT%z")

        return f"{time_str} ({obj.date.tzname()})"

    # noinspection PyMethodMayBeStatic
    def get_fullDescription(self, obj: Product):

        return obj.description

    # noinspection PyMethodMayBeStatic
    def get_description(self, obj: Product):
        return obj.description[:20]

    # noinspection PyMethodMayBeStatic
    def get_images(self, obj: Product):
        p: ProductImage
        # print(p.image.url)
        images = [
            {"src": image.image.url, "alt": image.alt}
            for image in obj.images.all()
        ]

        return images

    # noinspection PyMethodMayBeStatic
    def get_tags(self, obj: Product):
        return [tag.name for tag in obj.tags.all()]

    # noinspection PyMethodMayBeStatic
    def get_reviews(self, obj: Product):
        return [
            {
                "author": review.author.username,
                "email": review.author.email,
                "text": review.text,
                "rate": review.rate,
                "date": review.date.strftime("%Y-%m-%d %M:%S"),
            }
            for review in obj.reviews.all()
        ]

    # noinspection PyMethodMayBeStatic
    def get_specifications(self, obj: Product):
        return [
            {"name": specification.name, "value": specification.value}
            for specification in obj.specifications.all()
        ]

    @action(detail=True, methods=["get", "post"], url_path="review")
    def review(self, request, pk=None):
        product = self.get_object()

        if request.method == "GET":
            qs = product.reviews.all()
            serializer = ReviewSerializer(qs, many=True)
            return Response(serializer.data)

        # POST — создать отзыв для продукта
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()
        product.reviews.add(review)
        return Response(ReviewSerializer(review).data, status=201)


class TagSerializer(serializers.ModelSerializer):
    class Meta:

        model = Tag
        fields = "id", "name"

    id = serializers.SerializerMethodField()

    # noinspection PyMethodMayBeStatic
    def get_id(self, obj: Tag ):
        return obj.pk


class BasketModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Basket
        fields = (
            "id",
            "category",
            "price",
            "count",
            "date",
            "title",
            "description",
            "freeDelivery",
            "tags",
            "reviews",
            "rating",
        )

    id = serializers.IntegerField(min_value=1, source="product.pk")
    category = serializers.IntegerField(min_value=1, source="product.category.id")
    price = serializers.DecimalField(
        source="product.price", max_digits=10**9, decimal_places=2
    )
    count = serializers.IntegerField(min_value=1, source="product.count")
    date = serializers.DateTimeField(source="product.date")
    title = serializers.CharField(source="product.title")
    description = serializers.CharField(source="product.title")
    freeDelivery = serializers.BooleanField(source="product.freeDelivery")
    tags = TagSerializer(source="product.tags", many=True)
    reviews = ReviewSerializer(source="product.reviews", many=True)
    rating = serializers.FloatField(source="product.rating")
