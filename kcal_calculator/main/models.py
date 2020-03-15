from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    kcal = models.IntegerField(default=0)
    image = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def total_likes(self):
        return self.likes.count()
