from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
## 회원가입 빌트인 폼
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_safe, require_http_methods

# Create your views here.
def login(req):
    # 방법1
    # next_url = req.POST.get('next')
    # 방법2
    next_url = req.GET.get('next')
    if req.method=="POST":
        form = AuthenticationForm(req, req.POST)
        # 유효성검사
        print(form.data)
        if form.is_valid():
            #로그인
            auth_login(req, form.get_user())
            # next_url이 있냐없냐에 따라 다른 경로로 redirect
            return redirect(next_url) if next_url else redirect('app1:index')
        else:
            return HttpResponse('에러페이지입니다')
    else:
        form = AuthenticationForm()
        next = req.GET.get('next') # ????
        context ={
            'form':form,
            'next':next
        }
        return render(req, 'accounts/login.html', context)

def logout(req):
    auth_logout(req)
    return redirect('app1:index')

def signup(req):
    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)
        print(form.data)
        if form.is_valid():
            user = form.save()
            # 회원가입 한다음에 로그인처리까지.
            # 로그인시 로직과 다르게, 여기서 쓰는 모델폼CustomUserCreationForm은 get_user()메서드를 갖고있지 않기 때문에 쓰면 오류나고, form.save()의 반환값을 user로 받은 다음에 두번째 인자로 넣어줘야 한다.
            auth_login(req, user)
            return redirect('app1:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(req, 'accounts/signup.html', context)


@require_http_methods(['POST'])
def delete(req):
    user = req.user
    user.delete()
    auth_logout(req)
    return redirect('app1:index')

def update(req):
    if req.method=='POST':
        form = CustomUserChangeForm(instance = req.user)
        if form.is_valid():
            form.save()
            return redirect('app1:index')
    else:
        # 인자를 넣어줘야 기존 정보가 뜸.
        form = CustomUserChangeForm(instance = req.user)
        context = {
            'form':form
        }
        return render(req, 'accounts/update.html', context)

def change_password(req):
    if req.method == 'POST':
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            form.save()
            # 비밀번호면경하면 세션 끊겨서 로그아웃됨, 그래서 다시 업데이터해서 로그인상태 유지해줘야함. 이때 걍 개꿀모듈 또 쓰면 됨.
            update_session_auth_hash(req, form.user)
            return redirect('app1:index')
    else:
        form = PasswordChangeForm(req.user)
    context ={
        'form': form
    }

    return render(req, 'accounts/change_password.html', context)

