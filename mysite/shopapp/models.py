from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30)

def gen_path_to_avatar(instance: 'Avatar', filename: str) -> str:
    return f"avatars/{instance.pk}/{filename}"

class Avatar(models.Model):
    image = models.ImageField(upload_to=gen_path_to_avatar, null=True, blank=True)
    alt = models.CharField(max_length=255, blank=True)

    user = models.OneToOneField(User, related_name="avatar", on_delete=models.CASCADE, null=True, blank=True)