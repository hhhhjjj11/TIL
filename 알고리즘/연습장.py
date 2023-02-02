N = int(input())
li1 = list(map(int,input().split()))
M = int(input())
li2 = list(map(int,input().split()))

def bin_search(n, li):

    li.sort() # 5   [ -10 2 3 6 10 ]
    mid=len(li)//2  # 2
    leng = mid  # 2
    while True:
        if leng == 0 :
            if li[mid+1]==n or li[mid-1]==n:
                return 1
            return 0
        if n == li[mid]: # 10 == li[2](=3)
            return 1
        if n < li[mid]:
            leng//=2
            mid-=leng
        else:
            mid+=leng   # mid = mid +1 =3 


for item in li2:
    print(bin_search(item, li1),end=' ')
