from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )

    def str(self):
        return self.question_text
class Notification(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    is_seen = models.BooleanField()
    def __str__(self):
        return self.text
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # groups = models.ManyToManyField('Group', related_name='members')
    avatar = models.ImageField(default='profile_images/default.png', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
