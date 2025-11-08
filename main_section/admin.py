from django.contrib import admin

from main_section.models import (Manga)


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['name', 'cover', 'link']
    search_fields = ['name']