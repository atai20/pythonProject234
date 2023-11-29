from django.contrib import admin
from .models import User
from .models import Profile, Notification

class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "first_name", "last_name", "password"]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["avatar", "bio"]

admin.site.register(User, UserAdmin)
admin.site.register(Notification)

admin.site.register(Profile)
# Register your models here.
