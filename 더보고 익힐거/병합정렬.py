T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    res = 0

    cnt = 0

    def merge_sort(arr):
        def sort(low, high):
            if high - low < 2:
                return
            mid = (high+low)//2
            sort(low, mid)
            sort(mid, high)
            merge(low, mid, high)

        def merge(low, mid, high):
            temp = []
            l, h = low, mid

            global cnt

            if arr[mid-1] > arr[high-1]:
                cnt += 1

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

            for i in range(low, high):
                arr[i] = temp[i- low]

        return sort(0, len(arr))

    merge_sort(arr)

    res = arr[len(arr)//2]

    print(f'#{tc} {res} {cnt}')
