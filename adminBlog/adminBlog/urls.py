"""adminBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # blog_id 는 다른 이름으로 해도 되는데 views.py 에서 request와 같이 받는 이름을 맞춰줘야 한다.
    path('blog/<int:blog_id>/', detail, name='detail'),
    path('blog/new/', new, name='new'),
    path('blog/create/', create, name='create'),
    path('blog/delete/<int:blog_id>/', delete, name='delete'),
    path('blog/edit/<int:blog_id>/', edit, name='edit'),
]
