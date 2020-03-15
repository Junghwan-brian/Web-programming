from django import forms
from .models import Post


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'price', 'contents', 'src', 'img',
                  'img2', 'img3', 'img4', 'img5', 'category']
