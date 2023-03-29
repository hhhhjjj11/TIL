# 코드이해하기
# low_arr = merge_sort(^N)(arr[:mid])
# 각각의 호출된 함수에서 phase1이 끝난뒤 phase2가 마저 진행된다.
# 호출은 merge_sort(arr[:mid])의 배열의 크기가 1일때까지 호출된다.
# 따라서 마지막으로 호출된 함수의 리턴값은 arr이고 (즉, 크기가 1일때까지 계속 쪼갠다.)
# 그다음 마지막-1 번째 함수의 phase2가 실행이 된다.
# 그러면 merged_arr가 리턴된다.
# 그다음 마지막-2 번째 함수의 phase2가 실행이 된다.

# 근데 이렇게 하면 인덱스슬라이싱 써서 메모리 비효율임.
# 그래서 다른 최적화한 다른 코드를 써야함.

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    # phase1
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    # phase2
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


# 인덱스접근임.
# 함수안에 함수정의..
# 위의 코드와 마찬가지로
# 초항인덱스와 막항인덱스의 차이가 1일때 까지 계속호출
# 차이가 1인 경우 리턴 (마지막함수)
# 마지막-1 번 째 함수에서 merge(low,mid,high)실행 됨
# 머지는 원래 리스트인 arr의 각 항을 재할당 해주는 함수이므로 리턴이 없음.
# 다만 arr를 고쳐준다.

def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:  #왜 2인지 모르겠다. 1이어야 할 것 같은데. -> 항넘버가아니라 len(arr) 로 항의 크기로 넣을거라서 그런 듯.
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

                                            # 왼쪽의 첫번째랑 오른쪽의 첫번째 비교해서 작은애 넣고 커서 옮기고
    def merge(low, mid, high):              # 왼쪽이랑 오른쪽 중 하나가 소진될 때 까지.
        temp = []                           # 즉, 둘 다 남아 있을 동안은.
        l, h = low, mid                     # 즉, 커서가 둘다 오른쪽 끝보다 작을동안은.

        while l < mid and h < high:         # 비교해서 temp에 저장
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        # 첫번째 와일문을 빠져나왔다는 것은 왼쪽이나 오른쪽 둘 중 하나는 동났다는 것임.
        # 반대로 생각하면, 나머지에는 항이 남아있음.

        # 따라서, 다음의 경우를 생각해주어야한다.:
        # 왼쪽 리스트에 작은 값들이 많아서 먼저 다 쓰이는 경우 (이경우 오른쪽 배열만 남게 됨)
        # 반대의 경우 (이 경우 왼쪽 배열만 남게 됨)

        # 왼쪽 항이 남아있을 경우 1번 와일문이 실행 될테고,
        # 오른쪽 항이 남아있을 경우 2번 와일문이 실행 됨
        # 각각에서, 남은 항들을 모두 temp에 담아주면 됨. (이미 각각이 정렬된 상태임을 상기하자.)

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        # 이렇게 하면 모든 정렬이 끝난 것이고
        # 이제 temp에있는거를 순서대로 arr[low] 부터 arr[high]까지 넣어주면 된다.

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


# 다음처럼 바꾸어 보았다.

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



# 수업때 교수님이 작성해주신 코드
def msort(s, e):
    if s == e:
        return
    m = (s + e)//2
    msort(s, m)
    msort(m+1, e)
    l, r = s, m+1

    tmp= []

    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m:
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1
        elif r <= e:
            while r <= e:
                tmp[k] = arr[r]
                r += 1
                k += 1

    k = 0
    i = 0
    while i<k:
        arr[s + i] = tmp[i]
        i += 1
    return

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

