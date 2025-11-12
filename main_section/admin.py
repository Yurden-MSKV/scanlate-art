from django.contrib import admin

from main_section.models import (Manga, Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_picture', 'bio']

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['name', 'cover', 'link']
    search_fields = ['name']