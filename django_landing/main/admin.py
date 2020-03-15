from django.contrib import admin
from .models import Post
# Register your models here.

# admin에 등록해서 글을 작성할 수 있게 한다.
admin.site.register(Post)
