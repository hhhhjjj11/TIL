"""mypjt URL Configuration

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

# 식별자에 행위 넣지 않음. 근데 우리는 여태까지 url에 행위를 넣어왔음.
# 이것은 restful 하지 않음.
# 이제 이렇게 하지 말자.

urlpatterns = [
    # 잘못된 URI 구성
    # path('', views.index, name='index'),
    # path('create/', views.create, name='create'),
    # path('<int:pk>/', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.update, name='index'),
    # path('', views.delete, name='index'),

    # REST API 
    # 파라미터가 없는경우 끼리 합치고 있는경우 끼리 합친다. 
    # 그리고 http메소드로 분기할거임. 
    # 이렇게 함으로써 7개를 2개로 효율적으로 만들 수 있다.
    path('',views.article_list, name="article_lsit"),
    path('<int:pk>/', views.article_detail, name='article_detail'),

]
