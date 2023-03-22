from django.shortcuts import render, redirect

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

    # 1. 쿠키에 세션 데이터가 있는가?
    if not request.COOKIES.get('sessionid'):
        return redirect('accounts:login')

    # 2. request.user가 있는가?
    # 장고에서는 유저 정보를 request.user 안에 담고있다.
    if request.user:
        return redirect('accounts:login')