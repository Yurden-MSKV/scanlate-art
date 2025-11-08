from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категории'

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Тэги'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    post_content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Посты'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    comment_content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Комментарии'

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
