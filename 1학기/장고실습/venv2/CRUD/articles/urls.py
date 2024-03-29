from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'articles'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>/', views.detail, name = 'detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
