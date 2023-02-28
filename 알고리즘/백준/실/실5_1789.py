N = int(input()) # N=3

n=0
cnt = 0
while True :
    if N == 1 or N == 2:
        cnt += 1
        break
    
    n+=1   # n = 1 
    N-=n    # N =2
    
    cnt +=1  # cnt=1
    
    if N-n-1<=n+1 : 
        cnt+=1
        break

print(cnt)


# 주어진 조건을 쉽게 풀 수 있는 동치를 찾기.
# N-n-1<=n+1 이줄이 핵심 조건.