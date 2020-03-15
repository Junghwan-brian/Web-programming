from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField(label='먹은 음식')

    class Meta:
        model = Post
        fields = ['title', 'kcal', 'image']
