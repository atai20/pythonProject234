from django.contrib import admin

from .models import Choice, Question, Client, Post


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Client)

class QuestionAdmin(admin.ModelAdmin):
    list_display = [ "question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Post)
admin.site.register(Question, QuestionAdmin)
