from django import forms
from .models import Blog


class Blogform(forms.ModelForm):
    title = forms.CharField(max_length=50)
    time = forms.TimeField(label='시간')
    body = forms.Textarea()

    #  class Meta 구문은 이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 구문이다.(model=Blog)
    class Meta:
        model = Blog
        fields = '__all__'
