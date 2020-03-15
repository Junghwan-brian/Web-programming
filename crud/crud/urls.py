"""blog URL Configuration

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
from main.views import *
from about.views import about
from post.views import post
from contact.views import contact
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    # name으로 index로 지정해야 template에서 {% url 'index' %}로 쓴 index로 가게된다
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/', post, name='post'),
    path('post/<int:pk>', postdetail, name='detail'),
    path('contact/', contact, name='contact'),
    path('new/', new, name='new'),
    path('delete/<int:pk>', delete, name='delete'),
    path('update/<int:pk>', update, name='update'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 이미지를 볼 수 있게 한다.
