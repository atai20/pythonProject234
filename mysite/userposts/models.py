from django.db import models
from django.conf import settings

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from mptt.querysets import TreeQuerySet

from .choices import Vote

User = settings.AUTH_USER_MODEL

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
    img = models.ImageField(upload_to='media')
    up_total = models.PositiveIntegerField(default=0)
    down_total = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: "Post"
        verbose_name_plural: "Posts"
        indexes = [models.Index(fields=["created"]),
                   models.Index(fields=["user"])]

    def __str__(self):
        return self.title

class PostVotes(models.Model):

    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    voted_post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL, related_name='votes')
    value = models.SmallIntegerField(choices=Vote.choices, db_index=True)

class Comment(MPTTModel):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='post_comments')
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    body = models.TextField()
    up_total = models.IntegerField(default=0)
    down_total = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Post Comments"

    def __str__(self):
        return f"<{self.pk}: {self.user.username} -> {self.post.title}>"

class CommentVotes(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE, related_name='comments_votes')
    value = models.SmallIntegerField(choices=Vote.choices)
    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Post Comments"
