from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    dateCreate = models.DateTimeField()
    category = TaggableManager()

    def __str__(self):
        return self.title
