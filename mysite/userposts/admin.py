from django.contrib import admin
from .models import Post, CommentVotes, Comment, PostVotes
# Register your models here
admin.site.register(Post)
admin.site.register(PostVotes)
admin.site.register(Comment)
admin.site.register(CommentVotes)
