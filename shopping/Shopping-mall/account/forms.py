from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):

    # 아쉽게도 User 모델에서는 password_check 필드를 제공해주지 않는다.
    # 따라서 따로 password_check 필드를 직접 정의해줄 필요가 있다.
    # 입력 양식은 type은 기본이 text이다. 따라서 다르게 지정해주고 싶을 경우 widget을 이용한다.
    # widget=forms.PasswordInput()은 입력 양식을 password로 지정해주겠다는 뜻이다.
    password_check = forms.CharField(
        max_length=100, widget=forms.PasswordInput())

    # field_order는 만들어지는 입력양식의 순서를 정해준다.
    # 여기서 사용한 이유는 password 바로 밑에 password_check 입력양식을 추가시키고 싶어서이다.
    # 만약 따로 field_order를 지정해주지않았다면, password_check는 맨 밑에 생성된다.
    field_order = ['username', 'password', 'password_check',
                   'last_name', 'first_name', 'email']

    class Meta:
        model = User
        # 비밀번호를 칠때 안보이게 해준다. *가나옴.
        widgets = {'password': forms.PasswordInput}
        fields = ['username', 'password', 'last_name', 'first_name', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
