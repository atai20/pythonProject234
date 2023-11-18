from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # groups = models.ManyToManyField('Group', related_name='members')
    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
