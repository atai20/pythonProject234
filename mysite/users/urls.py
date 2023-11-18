from django.contrib import admin
from django.urls import path
from .views import LoginView, RegisterView, DashboardView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .forms import LoginForm

app_name = "core"
urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='core/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('upload/', views.simple_upload, name='upload'),

    path('register/', RegisterView.as_view(), name='register-view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-view'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
