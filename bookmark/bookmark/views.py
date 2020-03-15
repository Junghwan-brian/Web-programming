from django.shortcuts import render, redirect, get_object_or_404
# redirect는 함수내용이 다 사용되고 다시 돌아갈 페이지적용, get_object_or_404는 내용을 가져올 때 원하는 내용이 없을 때 404를 뿌려주는 기능.
from .models import Bookmark
from .forms import BookmarkForm
# Create your views here.


def list(request):
    list = Bookmark.objects.all()
    return render(request, 'bookmark/list.html',
                  {'list': list, })


def new(request):
    if request.method == 'POST':  # request가 POST방식이라면
        form = BookmarkForm(request.POST)
        # post 방식이라 데이터를 검증하는 과정이 있다.
        # 검증에 성공한 값들은 사전타입으로 제공 (form.cleaned_data)
        # 검증에 실패시 form.error 에 오류 정보를 저장
        if form.is_valid():
            bookmark = Bookmark()  # database bookmark
            # data를 정리하고 site_name을 넣는다
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            # return값에서 bookmark는 urls.py의 app_name에서 정의된 것이고 :list는 urls.py의 urlpatterns에서 정의한 list에대한 path의 name 부분이다.
            return redirect('bookmark:list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmark/new.html', {
        'form': form,
    })


def edit(request, pk):  # 아무글이나 수정하면 안되므로 pk를 받는다.
    bookmark = get_object_or_404(Bookmark, pk=pk)  # 전달받은 pk값으로 db내용을 조회한다.
    if request.method == 'POST':
        # 기존에 있던 값을 미리 뿌려줘야하므로(기존의 글을 가져오지 않으면 처음부터 다시 써야하므로)
        # instance를 지정해서 기존의 내용을 보여준다=>
        # bookmark = get_object_or_404(Bookmark, pk=pk)를 통해 넘어온 내용을 받는다.
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():  # form의 값이 있다면 => 즉 , bookmark에 값이 있다면.
            # site_name field에 site_name으로 넘어온 값을 넣는다.
            # form.is_valid() 를 실행하게 되면 cleaned_data dictionary가 생기게 된다.
            # bookmark는 객체이므로 bookmark.name을 쓴다.
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            # return으로 잘 수정되었나 볼 수 있는 bookmark 전체를 볼수있는 화면으로 전환.
            return redirect('bookmark:list')
    else:  # POST 값으로 넘어온 값이 없다면 수정하기 전의 페이지를 보여준다. 수정하기 전 페이지 접속시 보이는 화면을 출력해주는듯
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmark/edit.html', {
        # 기존의 파일을 수정해야하므로 bookmark 내용이 추가되었다.
        'bookmark': bookmark,
        'form': form,
    })


def delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == "POST":
        bookmark.delete()
        return redirect('bookmark:list')
