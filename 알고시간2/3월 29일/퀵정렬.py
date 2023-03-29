T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    def quicksort(arr):
        if len(arr)<2:
            return arr

        pivot = arr[len(arr)//2]

        small=[]
        big=[]
        equal=[]

        for i in range(len(arr)):
            if arr[i] > pivot:
                big.append(arr[i])
            elif arr[i] == pivot:
                equal.append(arr[i])
            else:
                small.append(arr[i])

        return quicksort(small) + equal + quicksort(big)


    res = quicksort(arr)[len(arr)//2]
    print(f'#{tc} {res}')