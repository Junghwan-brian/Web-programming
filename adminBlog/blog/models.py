from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    time = models.TimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        # 10글자가 넘어가면 글이 안보이게 하기 위함.
        return self.body[:10]
