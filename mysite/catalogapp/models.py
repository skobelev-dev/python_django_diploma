from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

from reviews.models import Review


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Tag(pk={self.pk}, name={self.name!r})"


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"Category(pk={self.pk}, name={self.name!r})"


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.DO_NOTHING
    )
    price = models.DecimalField(max_digits=10 * 6, decimal_places=2)
    count = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10**15 - 1),
        ],
    )
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=800)
    freeDelivery = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="products", null=True, blank=True)
    reviews = models.ManyToManyField(
        Review, related_name="products", null=True, blank=True
    )
    rating = models.FloatField(default=0)

    def __str__(self):
        return f"Product(pk={self.pk}, title={self.title!r})"


class Specifications(models.Model):
    products = models.ManyToManyField(Product, related_name="specifications")
    name = models.CharField(max_length=60)
    value = models.CharField(max_length=70)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)