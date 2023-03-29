arr = [12,3,4,55,66,33]

def merge_sort(low, high):
    if high - low < 2:  #왜 2인지 모르겠다. 1이어야 할 것 같은데.
        return
    mid = (low + high) // 2
    merge_sort(low, mid)
    merge_sort(mid, high)

    temp = []
    l, h = low, mid

    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[h])
            h += 1

    while l < mid:
        temp.append(arr[l])
        l += 1
    while h < high:
        temp.append(arr[h])
        h += 1

    # 이렇게 하면 모든 정렬이 끝난 것이고
    # 이제 temp에 있는거를 순서대로 arr[low] 부터 arr[high]까지 넣어주면 된다.

    for i in range(low, high):
        arr[i] = temp[i - low]


merge_sort(0,len(arr))
print(arr)