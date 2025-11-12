from django.shortcuts import render

from post_section.models import Post


def only_posts(request):
    posts = Post.objects.select_related('author__profile', 'category').prefetch_related('tags').all(

    ).order_by(
        '-created_at')

    context = {'posts': posts}

    return render(request, 'only_post_catalog.html', context)