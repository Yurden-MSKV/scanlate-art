from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from main_section import views as main_section_views
from job_section import views as job_section_views
from post_section import views as post_section_views
from scanlate_art import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_section_views.index),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('jobs/', include('job_section.urls')),
    path('posts/', include('post_section.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)