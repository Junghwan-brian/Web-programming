from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateField('date published')
    body = models.TextField()

# blog 작성했을 때 제목이 보이게 해준다.
    def __str__(self):
        return self.title