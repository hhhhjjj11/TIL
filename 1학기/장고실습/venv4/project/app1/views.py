from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .models import Article

# Create your views here.
def index(req):
    # articles = Article.objects.all()
    # context = {'articles':articles}

    response = render(req, 'app1/index.html')
    # set_cookie : 응답시 쿠키에 데이터를 담아서 보낼 수 있다.
    # 첫번째인자가 key, 두번째 인자가 value임.
    response.set_cookie('message','wow')
    return response

def create(request):
    # 로그인되지 않은 사용자는 로그인 페이지로 리다이렉션
    # 이때 로그인 한다음에 다시 글작성 페이지로 돌아오기 위해서 쿼리스트링을 이용.
    if not request.user.is_authenticated:
        # reverse: 전달받은 Name 에 매칭된 url을 문자열로 반환
        # return redirect(reverse('))
        print(reverse('accounts:login'))
        return redirect(reverse('accounts:login'+ f'?next={request.path}'))
        return redirect(f'/accounts/login?next={request.path}')
    # # 1. 쿠키에 세션 데이터가 있는가?
    # if not request.COOKIES.get('sessionid'):
    #     return redirect('accounts:login')

    # # 2. request.user가 있는가?
    # # 장고에서는 유저 정보를 request.user 안에 담고있다.
    # if request.user:
    #     return redirect('accounts:login')
    else:
        return render(request, 'app1/create.html')

def delete(req, pk):
    # 로그인 안된채로 삭제하면 -> 로그인 창먼저갔다가 -> 로그인되면 다시 상세페이지로
    if not req.user.is_authenticated:
        return redirect(reverse('accounts:login') + f'?next=/app1/detail/{pk}')
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')