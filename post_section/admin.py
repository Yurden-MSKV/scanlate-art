from django.contrib import admin

from post_section.models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('author', 'view_count', 'like_count', 'dislike_count')
    list_display = ['title', 'author', 'category', 'display_tags', 'post_content', 'created_at', 'view_count',
                    'like_count', 'dislike_count']
    search_fields = ['category']

    def display_tags(self, obj):
        return ", ".join([tag.tag_name for tag in obj.tags.all()])

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Если объект создается впервые
            obj.author = request.user
        super().save_model(request, obj, form, change)

    display_tags.short_description = 'Теги'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']