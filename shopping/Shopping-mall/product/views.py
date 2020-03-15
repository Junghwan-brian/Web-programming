from django.shortcuts import render
from main.models import Post
# Create your views here.


def product(request):
    postAll = Post.objects.all()
    return render(request, 'product/product.html', {'postAll': postAll})
