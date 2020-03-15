from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    dataCreat = models.DateTimeField()
    Category = models.TextField()

    def __str__(self):
        # 입력받은 title이 제목이라는 걸 장고에게 알려준다.
        return self.title
