# 퀵정렬
# 리스트 정 가운데 값을 pivot으로 선택
# 반복문을 통해 각 값을 pivot과 비교 후 크/작에 추가
# 각 배열을 대상으로 재귀호출

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    small = []
    big = []
    equal = []
    for i in range(len(arr)):
        if arr[i] > pivot:
            big.append(arr[i])
        elif arr[i] < pivot:
            small.append(arr[i])
        else:
            equal.append(arr[i])
    return quicksort(small) + equal + quicksort(big)

arr = [2,345,62,3,4,5,11]

print(quicksort(arr))

