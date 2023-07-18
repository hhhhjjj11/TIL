from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model

# Create your views here.
def login(req):
    if req.method == "POST":
        form = AuthenticationForm(req,req.POST)
        if form.is_valid():
            auth_login(req, form.get_user()) 
            return redirect('movies:index')
    form = AuthenticationForm()
    context ={
        'form': form
    }
    return render(req, 'accounts/login.html', context)

def logout(req):
    if req.user.is_authenticated:
        auth_logout(req)
    return redirect('movies:index')

def signup(req):
    if req.method=="POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            auth_login(req, user)
            return redirect('movies:index')
    
    form = CustomUserCreationForm()
    context={
        'form':form
    }
    return render(req, 'accounts/signup.html', context)

def update(req):
    if req.method == "POST":
        form = CustomUserChangeForm(req.POST, instance= req.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')

    form = CustomUserChangeForm(instance = req.user)
    context = {
        'form':form
    }
    return render(req, 'accounts/update.html', context)

def delete(req):
    req.user.delete()
    auth_logout(req)
    return redirect('movies:index')

def change_password(req):
    if req.method=="POST":
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user) # req.user 넣으면 안되나??/
            return redirect('movies:index')
        
    form = PasswordChangeForm(req.user)
    context ={
        'form':form
    }
    return render(req, 'accounts/change_password.html', context)
    
def profile(req, username):

    person = get_user_model().objects.get(username= username)
    context= {
        'person':person,
    }

    return render(req, 'accounts/profile.html', context)

def follow(req, username):
    if not req.user.is_authenticated:
        return redirect('accounts:login')
    # 만약에 그 유저가 이미 있으면
    user = get_user_model().objects.get(username = username)
    # 만약에 유저가 그 유저가 이미 db의 user 에 있는 애면 
    if req.user != user:
        if user.followers.filter(pk=req.user.pk).exists():
            user.followers.remove(req.user)
        else:
            user.followers.add(req.user)
    return redirect('accounts:profile',username)