from django.shortcuts import render
from .models import Pet, PetSitter
from django.db import connection
from django.db import reset_queries


# 함수의 처음과 끝에 뭔가 처리를 해주도록 다음과 같이 로직을 작성.
def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs): # 인자를 이렇게 넣어주면 인자를 아무거나 다 받겠다는 의미임
        reset_queries()
        origin_func()

        query_info = connection.queries
        for query in query_info:
            print(query['sql'])

    return wrapper

# def get_pet_data():

#     pets = Pet.objects.all()
#     for pet in pets:
#         print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')


# def get_pet_data():
#     reset_queries()

#     pets = Pet.objects.all()
#     for pet in pets:
#         print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')

#     query_info = connection.queries
#     for query in query_info:
#         print(query['sql'])


# 위에꺼를 데코레이터 쓰는 버전으로 바꿔주면
@get_sql_queries
def get_pet_data():

    pets = Pet.objects.all()
    for pet in pets:
        print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')


# 위에꺼를 데코레이터 쓰는 버전으로 바꿔주면
@get_sql_queries
def get_pet_data():

    pets = Pet.objects.all().select_related('pet_sitter') # 이렇게 해주면 레이지로딩이 아니라 여기서 db에잇는걸 불러옴. 포문안에서 여러번 db콜 할필요가 없어짐. 문제해결
    for pet in pets:
        print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')

