from django import forms
from .models import Post
from taggit.forms import TagWidget, TagField


class Postform(forms.ModelForm):
    category = TagField()

    class Meta:
        model = Post
        fields = ['title', 'contents', 'img', 'category']
