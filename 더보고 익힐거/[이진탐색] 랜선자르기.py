# 이진탐색 문제 : 경계를 어떻게처리할것인지.... 경계를 어덯게 옮기고 
# 어떤 값을 리턴할 것인지.... 존나헷갈림.

K, N  = map(int,input().split())

list = [int(input()) for _ in range(K)]

total = sum(list)

R = total//N

L = 1

while L <= R:
    mid = (R+L)//2
    cnt = 0
    for i in range(K):
        cnt += list[i]//mid
    if cnt < N :
        R  = mid -1 
    elif cnt == N:
        L = mid + 1
    else:
        L = mid + 1  
print(R)

# 가운데 찍어보고 만약에 좀 이거보다 크면 안되고 작아야한다 하면 
# 오른쪽경계를 mid 나 mid-1로 옮기고 
# 반대로 이거보다 좀 커야한다 하면 
# 왼족경계를 mid 나 mid+1로 옮기고
# 새로운 경계들의 중점을 또 찍고 같은 과정을 반복한다. 
# 

# 생각
# 되고 되고 되고 되고 되고 안되고 안되고 안되고
