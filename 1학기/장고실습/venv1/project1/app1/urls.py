"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app1"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test1/', views.test1, name='test'), # include 테스트
    path('<int:num1>/<int:num2>', views.variableRouting), # variableRouting
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('articles/', views.articles, name='articles'),
]
    