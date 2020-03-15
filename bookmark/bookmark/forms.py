from django import forms
from .models import Bookmark
# 기존의 내용을 불러오기 위해서는 form을 가져올 때 설정해주어야 한다.


# forms.ModelForm (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성..
# 즉,
# site_name = forms.CharField(label='사이트명') ,url = forms.CharField(label='주소') 를 안쓰고
# class Meta에서 model=Bookmark만 설정해줘도 괜찮음.
# 반면, forms.form 은 설정을 해줘야함.
# class PostForm(forms.Form):
# site_name = forms.CharField(label='사이트명')
# url = forms.CharField(label='주소')

class BookmarkForm(forms.ModelForm):
    site_name = forms.CharField(label='사이트명')
    url = forms.CharField(label='주소')

    class Meta:  # 전체의 option을 잡아주는 내용이다
        model = Bookmark
        # fields = ['site_name', 'url']  '__all__' 설정시 전체 필드 추가
        fields = '__all__'
