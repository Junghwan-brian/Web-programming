from django.shortcuts import render, redirect
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(
                request, username=username, password=password)
            # authenticate를 통해 DB의 username과 password를 클라이언트가 요청한 값과 비교한다.
            # 만약 같으면 해당 객체를 반환하고 아니라면 none을 반환한다.
            if user is not None:
                auth.login(request, user=user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': form, 'error': '아이디나 비밀번호가 일치하지 않습니다.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.last_name = form.cleaned_data['last_name']
                user.first_name = form.cleaned_data['first_name']
                user.save()
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'signup.html', {'error': 'password가 다릅니다'})
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
