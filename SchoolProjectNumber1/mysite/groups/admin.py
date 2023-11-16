from django.contrib import admin
from .models import Group


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ["profiles", "group_name", "group_description", "img"]


admin.site.register(Group)
