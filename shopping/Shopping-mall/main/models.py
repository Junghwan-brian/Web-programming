from django.db import models

# Create your models here.
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=50)
    price = models.TextField()
    contents = models.TextField()
    src = models.TextField()
    img = models.ImageField()
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    img4 = models.ImageField(null=True, blank=True)
    img5 = models.ImageField(null=True, blank=True)
    dateCreate = models.DateTimeField(auto_now_add=True)
    category = TaggableManager()

    def __str__(self):
        return self.title
# 주요 Field Option
# 필드옵션 : 필드마다 고유 옵션이 존재, 공통 적용 옵션도 있음
# null (DB 옵션) : DB 필드에 NULL 허용 여부 (디폴트 : False)
# unique (DB 옵션) : 유일성 여부 (디폴트 : False)
# blank : 입력값 유효성 (validation) 검사 시에 empty 값 허용 여부 (디폴트 : False)
# default : 디폴트 값 지정. 값이 지정되지 않았을 때 사용
# verbose_name : 필드 레이블. 지정되지 않으면 필드명이 쓰여짐
# validators : 입력값 유효성 검사를 수행할 함수를 다수 지정
# 각 필드마다 고유한 validators 들이 이미 등록되어있기도 함
# 예 : 이메일만 받기, 최대길이 제한, 최소길이 제한, 최대값 제한, 최소값 제한 등
# choices (form widget 용) : select box 소스로 사용
# help_text (form widget 용) : 필드 입력 도움말
# auto_now_add : Bool, True 인 경우, 레코드 생성시 현재 시간으로 자동 저장
