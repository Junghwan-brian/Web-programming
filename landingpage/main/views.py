from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST.get('check', ''):
            username = request.POST['name']
            email = request.POST['email']
            user = User.objects.create_user(
                username=username, email=email
            )
            user.last_name = request.POST['name']
            user.save()
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('/', {'error': 'You have to agree.'})
    return render(request, 'index.html')
