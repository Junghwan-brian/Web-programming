from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    postAll = Post.objects.all()
    # index.html에 파이썬 문법이 들어가는 데 이걸 html,css,js로 해석해서 사용자에게
    # 넘겨준다는 의미다.
    return render(request, 'main/index.html', {"postAll": postAll})
