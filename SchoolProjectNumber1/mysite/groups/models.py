from django.db import models
from users.models import Profile

# Create your models here.

class Group(models.Model):
    profiles = models.ManyToManyField(Profile)
    group_name = models.CharField(max_length=100)
    group_description = models.TextField(max_length=400)
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.group_name


# Create your models here.
