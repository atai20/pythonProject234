from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    postname = models.CharField(max_length=100)
    postauth = models.CharField(max_length=100)
    postdes = models.TextField(max_length=400)
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.postname
