from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
# Create your views here.
from .forms import Postform
from django.utils import timezone


def index(request):
    postAll = Post.objects.all()
    return render(request, 'main/index.html', {'postAll': postAll})


def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/postdetail.html', {'post': post})


def new(request):
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.img = form.cleaned_data['img']
            post.dateCreate = timezone.datetime.now()
            post.category = form.cleaned_data['category']
            post.save()
            return redirect('/post/'+str(post.pk))
    else:
        form = Postform()
        return render(request, 'main/new.html', {'form': form})


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')


def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.img = form.cleaned_data['img']
            post.dateCreate = timezone.datetime.now()
            post.category = form.cleaned_data['category']
            post.save()
            return redirect('/post/'+str(post.pk))
    else:
        form = Postform(instance=post)
        return render(request, 'main/update.html', {'form': form})
