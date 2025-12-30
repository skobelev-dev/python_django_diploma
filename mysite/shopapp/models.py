from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)


def gen_path_to_avatar(instance: "Avatar", filename: str) -> str:
    return f"avatars/{instance.pk}/{filename}"


class Avatar(models.Model):
    image = models.ImageField(upload_to=gen_path_to_avatar, null=True, blank=True)
    alt = models.CharField(max_length=255, blank=True)

    user = models.OneToOneField(
        User, related_name="avatar", on_delete=models.CASCADE, null=True, blank=True
    )


class Payment(models.Model):
    number = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10 ** 15 - 1, "15 цифр"),
        ],
    )
    name = models.CharField(max_length=35)
    month = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12),
        ]
    )
    year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(2000, "Год от 2000"),
            MaxValueValidator(2099, "Год до 2099"),
        ],
    )
    code = models.CharField(
        max_length=3, validators=[RegexValidator(r"^[0-9]{3}$", )]
    )


class Category(models.Model):
    name = models.CharField(max_length=40)


class Review(models.Model):
    author = models.ForeignKey(User, related_name="reviews", on_delete=models.DO_NOTHING)
    text = models.TextField(max_length=880)
    rate = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5, "5-ти бальная система"),
        ],
    )
    date = models.DateTimeField(auto_now_add=True)


def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    pk: 'Product.pk' = instance.product.pk
    return f"products/product_{pk}/{filename}"


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name = "images")

    image = models.ImageField(upload_to=product_images_directory_path)

    alt = models.CharField(max_length=50)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product", on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10*6, decimal_places=2)
    count = models.IntegerField(
            validators=[
                MinValueValidator(0),
                MaxValueValidator(10 ** 15 - 1),
            ],
    )
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=800)
    freeDelivery = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="products")
    reviews = models.ManyToManyField(Review, related_name="products")


class Satus(models.TextChoices):
    ACCEPTED = 'accepted'
    NOT_ACCEPTED = 'not accepted'

class DeliveryType(models.TextChoices):
    FREE = 'free', 'Бесплатная доставка'
    PAID = 'paid', 'Платная доставка'

class PaymentType(models.TextChoices):
    ONLINE = 'online', 'Онлайн'
    CASH = 'cash', 'Наличными'

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # Как я полагаю: имя, почта и телефон - пользователя совершившего заказ
    user = models.ForeignKey(User, related_name="orders", on_delete=models.DO_NOTHING)
    deliveryType = models.CharField(max_length=20, choices=DeliveryType.choices, default=DeliveryType.FREE)
    paymentType = models.CharField(max_length=20, choices=PaymentType.choices, default=PaymentType.ONLINE)
    totalCost = models.DecimalField(max_digits=10**9, decimal_places=2)
    status = models.CharField(max_length=20, choices=Satus.choices, default=Satus.ACCEPTED)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    products = models.ManyToManyField(Product, related_name="orders")
