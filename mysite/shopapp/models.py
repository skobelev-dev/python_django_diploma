from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30)

def gen_path_to_avatar(instance: 'Avatar', filename: str) -> str:
    return f"avatars/{instance.pk}/{filename}"

class Avatar(models.Model):
    image = models.ImageField(upload_to=gen_path_to_avatar)
    alt = models.CharField(max_length=255, blank=True)

