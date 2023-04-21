"""project URL Configuration

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

urlpatterns = [
    path('TEST/',views.test),
    path('save-deposit-products/', views.save_deposit_products), # 정기예금 상품 목록 DB에 저장
    path('deposit-products/', views.deposit_products), # 전체 정기예금 상품 목록 출력 & 데이터 삽입
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_product_options),         # 특정 상품의 옵션 리스트 출력
    path('deposit-products/top-rate/', views.top_rate), # 가입 기간에 상관없이 최고 금리가 가장 높은 금융 상품과 해당 상품의 옵션 리스트 출력
]
