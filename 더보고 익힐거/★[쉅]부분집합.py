arr = [ 1,2,3,4,5,6,7,8,9,10,11,12 ]

n = len(arr)

sub = []


for i in range(1<<n): # 부분집합의 갯수만큼.
    s=set()  
    for j in range(n):  # 각 항의 인덱스에 대하여    
        if i & (1<<j):      
        # & : 비트 연산자.  1<<j 는 2^j이고 이는 맨앞자리가 1이고 나머지가 0 인 j+1자리의 이진수임.
        # 예) 1<<3 = 2^3 = 100(2)  1<<6 = 2^6 = 1000000(2)
            s.add(arr[j])
    if len(s) != 0:
        sub.append(s)


T = int(input())

for tc in range(1,T+1):
    
    N,K =map(int,input().split())

    res = 0 

    for subset in sub:
        if len(subset) == N and sum(subset) ==K:
            res+=1

    print(f'#{tc} {res}')