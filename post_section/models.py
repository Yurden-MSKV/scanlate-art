import re

from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги'
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    post_content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.author} — {self.created_at}'

    def get_short_content(self, max_length=500):
        """
        Возвращает укороченное содержимое без изображений и с заменой &nbsp; на пробелы
        """
        # Удаляем все теги img
        content_no_images = re.sub(r'<img[^>]*>', '', self.post_content)

        # Заменяем &nbsp; на обычные пробелы
        content_no_nbsp = re.sub(r'&nbsp;', ' ', content_no_images)

        # Получаем чистый текст
        text_only = re.sub(r'<[^>]*>', '', content_no_nbsp)

        # Обрезаем текст
        if len(text_only) > max_length:
            return text_only[:max_length] + '...'
        return text_only

    def get_short_content_safe(self, max_length=500):
        """
        Безопасная версия для использования в шаблонах
        """
        from django.utils.safestring import mark_safe
        return mark_safe(self.get_short_content(max_length))

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    comment_content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0, editable=False)
    dislike_count = models.IntegerField(default=0, editable=False)

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author} — {self.created_at}'

class CommentView(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_view = models.BooleanField(default=False)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    is_like = models.BooleanField(default=False)
    is_dislike = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Лайки'
        verbose_name_plural = 'Лайки'
