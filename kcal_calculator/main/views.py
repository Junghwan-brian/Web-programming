import re
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def main(request):
    posts = Post.objects.all()
    total_kcal = 0
    for post in posts:
        total_kcal += post.kcal
    return render(request, 'main.html', {'posts': posts, 'total_kcal': total_kcal})


@login_required
def post_like(request, pk):
    # 포스트 정보 받아옴
    post = get_object_or_404(Post, pk=pk)
    # 사용자 정보 받아옴
    user = User.objects.get(username=request.user)
    # 좋아요에 사용자가 존재하면
    if post.likes.filter(id=user.id).exists():
        # 사용자를 지움
        post.likes.remove(user)
    else:
        # 아니면 사용자를 추가
        post.likes.add(user)
    # 포스트로 리디렉션
    return redirect('/')


# 해당 함수는 이제 login 되어야만 사용이 가능하다.
# 만일 로그인하지 않은 채로 실행 시 page를 찾을 수 없습니다.가 화면에 뜨게된다.
@login_required  # @login_required를 함수 앞에 써준다.
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post': post})


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'create.html', {'form': form})


@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
        return render(request, 'update.html', {'form': form})


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
