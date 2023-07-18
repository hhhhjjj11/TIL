from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import numpy as np
import pandas as pd

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

@api_view(['GET'])
def csv(req):
    # def file_open_by_numpy():
    #     # np.loadtxt(구분자 = ',', 데이터 타입: string)
    #     np_arr = np.loadtxt('./test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
    #     return np_arr

    # arr = file_open_by_numpy()
    # columns=arr[0]
    # arr = np.delete(arr, 0, 0)
    # print(arr)
    # df = pd.DataFrame(arr, columns=columns)
    df = pd.read_csv('./test_data.CSV', encoding='cp949')

    df.fillna("NULL", inplace=True)
    print('ddd')
    print(df)
    data = df.to_dict('records')

    return JsonResponse({'data': data})

@api_view(['GET'])
def age(req):

    df = pd.read_csv('./test_data.CSV', encoding='cp949')

    df['나이'].fillna(float("Nan"), inplace=True)

    average = df['나이'].mean()

    closest_to_40 = df['나이'].sub(average).abs().idxmin()
    closest_to_40_index = df['나이'].sub(average).abs().sort_values().head(10).index
 
    data = df.loc[closest_to_40_index].to_dict('records')

    return JsonResponse({'data': data})