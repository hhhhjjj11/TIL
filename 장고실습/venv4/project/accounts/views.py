from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse

# Create your views here.
def login(req):
    if req.method=="POST":
        form = AuthenticationForm(req, req.POST)
        # 유효성검사
        print(form.data)
        if form.is_valid():
            #로그인
            auth_login(req, form.get_user())
            return redirect('app1:index')
        else:
            return HttpResponse('에러페이지입니다')
    else:
        form = AuthenticationForm()
        context ={
            'form':form
        }
        return render(req, 'accounts/login.html', context)

def logout(req):
    auth_logout(req)
    return redirect('app1:index')