# 객체가 없으면 404 에러를 띄워준다.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import Blogform
# Create your views here.


def index(request):
    postAll = Blog.objects.all()
    return render(request, 'index.html', {'postAll': postAll})


def detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'post': post})


def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = Blogform(request.POST, instance=blog)
        # form.is_valid() 를 실행하게 되면 cleaned_data dictionary가 생기게 된다.
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.time = timezone.datetime.now()
            blog.body = form.cleaned_data['body']
            blog.save()
            return redirect('/blog/'+str(blog.id))
    else:  # POST 값으로 넘어온 값이 없다면 수정하기 전의 페이지를 보여준다.
        form = Blogform(instance=blog)
    return render(request, 'edit.html', {'blog': blog, 'form': form})


def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    # name=title인 것을 Get방식으로 가져온다.
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    # 현재시간을 넣어준다.
    blog.time = timezone.datetime.now()
    # 객체를 변형후 save를 해준다. 삭제를 해주고도 save를 해야한다.
    blog.save()
    # redirect안에는 url string이 들어가야하는데 blog.id는 숫자여서 str으로 바꿔준다.
    return redirect('/blog/' + str(blog.id))


def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')
