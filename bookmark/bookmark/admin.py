from django.contrib import admin

# Register your models here.
# models로부터 생성한 class인 Bookmark를 불러온다
from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'url']


admin.site.register(Bookmark, BookmarkAdmin)
