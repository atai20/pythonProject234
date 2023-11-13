from django.contrib import admin
from django.urls import path
from .views import LoginView, RegisterView, DashboardView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "core"
urlpatterns = [
    path('login/', LoginView.as_view(), name='login-view'),
    path('upload/', views.simple_upload, name='upload'),

    path('register/', RegisterView.as_view(), name='register-view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
