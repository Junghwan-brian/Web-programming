from django.urls import path
from .views import *
app_name = 'bookmark'  # app 이름 생성 그냥 동일하게햇다.

urlpatterns = [
    # 첫 main화면에 접속했을 때 list라는 뷰 함수를 실행, url을 추적하기 위해 list라는 이름을 지어준다.
    path('', list, name='list'),
    path('new/', new, name='new'),
    path('edit/<int:pk>', edit, name='edit'),  # edit에서 북마크의 고유한 pk값을 변수로 받는다.
    path('delete/<int:pk>', delete, name='delete'),
]
