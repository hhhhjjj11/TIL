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
from django.urls import path
from . import views

app_name ="movies"
urlpatterns = [
    path('', views.index, name = "index" ),
    path('create/', views.create, name="create"),
    path('<int:movie_pk>/', views.detail, name="detail"),
    path('<int:movie_pk>/update/', views.update, name="update"),
    path('<int:movie_pk>/delete/', views.delete, name="delete"),
    path('<int:movie_pk>/comments/', views.comments_create, name="comment_create"),
    path('<int:movie_pk>/comments/<int:commetn_pk>/delete/', views.comments_delelte, name="comment_delete"),
    path('<int:movie_pk>/likes/', views.likes, name="likes"),
]
