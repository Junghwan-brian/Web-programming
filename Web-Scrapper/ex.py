# %%
from bs4 import BeautifulSoup

str = '<body> 이 글은 예시를 위해 html 태그를 제거하는 방법에대한 내용이다. <br></br> 이 라이브러리로 html을 제거함. </body>'

str = BeautifulSoup(str, 'html.parser').get_text()
print(str)
