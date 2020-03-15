from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def detail(request):
    return render(request, 'detail.html')

def result(request):
    # post는 id 나 password같은 보여지면 안되는 것에 사용한다.
    # get은 보여져도 상관없는 데이터일 때 사용한다. => url 창에 입력값이 보인다.
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    max_val=0
    reward=''
    for k,v in word_dictionary.items():
        if v>=max_val:
            reward=k
            max_val=v
    word_count = {}
    for word in word_list:
        word_count[word] = len(word)
    max_num=0
    long_word=''
    for k,v in word_count.items():
        if v>=max_num:
            max_num=v
            long_word=k
    return render(request, 'result.html', {'fulltxt': full_text, 'total': len(word_list), 'word_dic': word_dictionary.items(),'reward':reward,'max_val':max_val,'long_word':long_word})