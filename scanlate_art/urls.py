from django.contrib import admin
from django.urls import path
from main_section import views as main_section_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_section_views.index)
]
