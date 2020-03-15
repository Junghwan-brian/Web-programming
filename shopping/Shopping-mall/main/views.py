from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import Postform
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    postAll = Post.objects.all()
    return render(request, 'main/index.html', {'postAll': postAll})


@login_required
def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/postdetail.html', {'post': post})


@login_required
def new(request):
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Postform()
    return render(request, 'main/new.html', {'form': form})


@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/post/'+str(post.pk))
    else:
        form = Postform(instance=post)
        return render(request, 'main/update.html', {'form': form})


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
