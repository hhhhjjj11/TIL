# 정답

N = int(input())
li = list(map(int,input().split()))
M = int(input())
li2 = list(map(int,input().split()))
li.sort()

def bin_search(n):

    L = 0
    R = len(li)-1
    while True:
        if R < L :   # R - L < 1 로 하면 R = L 인 경우에도 break걸어서 엣지케이스를 놓침. 
            break

        M = (L+R)//2
        
        if n == li[M] : 
            return 1
        elif n > li[M] :
            L = M + 1  # L = M 이 아니라 한칸 옮겨준다는 점 
        else : 
            R = M - 1
    return 0 
   

    
for item in li2:
    print(bin_search(item),end=' ')



# 삽질한거

# N = int(input())
# li1 = list(map(int,input().split()))
# M = int(input())
# li2 = list(map(int,input().split()))

# def bin_search(n, li):

#     li.sort() # 5   [ -10 2 3 6 10 ]
#     mid=len(li)//2  # 2
#     leng = mid  # 2
#     while True:
#         if leng == 0 :
#             if li[mid+1]==n or li[mid-1]==n:
#                 return 1
#             return 0
#         if n == li[mid]: # 10 == li[2](=3)
#             return 1
#         if n < li[mid]:
#             leng//=2
#             mid-=leng
#         else:
#             mid+=leng   # mid = mid +1 =3 


# for item in li2:
#     print(bin_search(item, li1),end=' ')

# 이진판별
# 내 나름대로 시도했었는데 
# 가운데 점과 양쪽 구간길이를 잡고 구간길이를 반씩 나눠서 더하거나 빼거나.이렇게 하면 안된다
# 홀 짝 때문에 따져야할게 좆같다 