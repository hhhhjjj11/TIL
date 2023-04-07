from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(req):
    if req.method == "POST":
        form = AuthenticationForm(req,req.POST)
        if form.is_valid():
            auth_login(req, form.get_user())
            return redirect('movies:index')
    
    else:
        form = AuthenticationForm()
        context = {
            'form':form,
        }
        return render(req, 'accounts/login.html', context)

@require_POST    
def logout(req):
    auth_logout(req)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def signup(req):
    if req.method == "POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            auth_login(req,user)
            return redirect('movies:index')
        else:
            context = {
                'form':form
            }
            return render(req, 'accounts/signup.html', context)
    else:
        form = CustomUserCreationForm()
        context ={
            'form': form
        }
        return render(req, 'accounts/signup.html', context)
    

@require_http_methods(['GET', 'POST'])
def update(req):
    if req.method == "POST":
        form = CustomUserChangeForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance = req.user)
        context = {
            'form':form
        }
        return render(req, 'accounts/update.html',context)
    
    
@require_POST  
def delete(req):
    user = req.user
    user.delete()
    auth_logout(req)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def password(req):
    if req.method == "POST":
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(req.user)
    
    context = {
        'form' : form
    }

    return render(req, 'accounts/change_password.html', context)