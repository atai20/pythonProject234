from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "polls"
urlpatterns = [
    path('post/', views.post_view, name='post'),
    path('create_post/', views.CreateView.as_view(), name='post'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
