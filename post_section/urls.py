from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from post_section import views as post_section_views

urlpatterns = [
    path('', post_section_views.only_posts, name='post_section'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)