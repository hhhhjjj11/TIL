from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import DepositProduct,DepositOptions
from rest_framework.response import Response
from .serializers import DepositProductSerializer, DepositOptionsSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

import requests

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'


@api_view(['GET'])
def test(req):
    json = {
        'dd':'dd'
    }
    return Response(json)


def api_test(req):
    URL = BASE_URL + 'depositProductsSearch.json'
    print('apikey', settings.API_KEY)
    params = {
        'auth': settings.API_KEY,
        # 금융회사 코드 020000(은행)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response= requests.get(URL, params=params)
    return response  

@api_view(['GET'])
def save_deposit_products(req):
    data = api_test(req).json()
    products = data['result']

    for product in products['baseList']: 
        try:
            product_inDB = DepositProduct.objects.get(fin_prdt_cd= product["fin_prdt_cd"])

        except:
            serializer = DepositProductSerializer(data = product)
            if serializer.is_valid(raise_exception = True):
                serializer.save()

    for option in products['optionList']:

        try:
            option_inDB = DepositProduct.objects.get(fin_prdt_cd= product["fin_prdt_cd"])

        except:
            serializer = DepositProductSerializer(data = product)
            if serializer.is_valid(raise_exception = True):
                serializer.save()



        for key in option.keys():
            if option[key] == None:
                option[key] = -1

        product = DepositProduct.objects.get(fin_prdt_cd = option['fin_prdt_cd'])
        serializer = DepositOptionsSerializer(data = option)
        if serializer.is_valid(raise_exception=True): 
            serializer.save(fin_prdt_cd=product)      

    return Response(status = status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def deposit_products(req):
    if req.method == 'GET':
        products = DepositProduct.objects.all()
        serializer = DepositProductSerializer(products, many=True)
        return Response(serializer.data)

    elif req.method == 'POST':
        serializer = DepositProductSerializer(data = req.data)
        if serializer.is_valid(raise_exception=True):
            # raise_exception = True // 유효성 검사 실패시 400상태코드 반환.
            serializer.save()
            return Response( status =status.HTTP_201_CREATED )


@api_view(['GET'])
def deposit_product_options(req,fin_prdt_cd):
    product = get_object_or_404(DepositProduct, fin_prdt_cd=fin_prdt_cd) 
    options = product.depositoptions_set.all() # 모델이름으로
    serializers = DepositOptionsSerializer(options, many = True)
    return Response(serializers.data)


@api_view(['GET'])
def top_rate(req):
    option = DepositOptions.objects.order_by('intr_rate2').first()
    print('option',option)
    prdt_id = option.fin_prdt_cd.pk
    print(f'id: {prdt_id}')
    products = DepositProduct.objects.get(pk= prdt_id)
    print('products',products)
    
    serializers = DepositProductSerializer(products)

    return Response(serializers.data)
