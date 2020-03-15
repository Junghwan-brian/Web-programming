from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('delete/<int:pk>', delete, name='delete'),
    path('update/<int:pk>', update, name='update'),
    path('detail/<int:pk>', detail, name='detail'),
    path('like/<int:pk>', post_like, name='post_like'),
]
