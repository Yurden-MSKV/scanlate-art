from django.contrib.auth.models import User
from django.db import models

def profile_pic_path(instance, filename):
    return f'profile/images/{instance.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Профили'

def cover_path(instance, filename):
    return f'manga/covers/{instance.id}/{filename}'

class Manga(models.Model):
    name = models.CharField(max_length=150)
    cover = models.ImageField(upload_to=cover_path, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'
