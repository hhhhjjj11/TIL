N = int(input())
li1 = list(map(int,input().split()))
M = int(input())
li2 = list(map(int,input().split()))
li1.sort()

def bin_search(n):

    mid=len(li1)//2  # 2
    leng = mid  # 2
    while True:
        if n == li1[mid]: # 10 == li[2](=3)
            return 1
        if leng == 1 :
            if mid == 0:
                return 0
            elif mid == len(li1)-1:
                return 0
            elif li1[mid+1]==n or li1[mid-1]==n:
                return 1
            return 0
        if n < li1[mid]:
            leng+=1
            leng//=2
            mid-=leng
        else:
            leng+=1
            leng//=2
            mid+=leng   # mid = mid +1 =3 


for item in li2:
    print(bin_search(item),end=' ')


# 이진판별을 내 나름대로 짜봤다. 
# 가운데 숫자(li[mid])와 양쪽 폭(leng)을 변수로 잡고 
# 근데 이렇게 하면 안된다
# 왜 이렇게 하면 안되는건지 생각해보았다.
# 대충 정리하면 다음과 같다.
# 1. 