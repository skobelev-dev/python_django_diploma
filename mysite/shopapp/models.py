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
    number = models.PositiveIntegerField(max_length=15)
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
