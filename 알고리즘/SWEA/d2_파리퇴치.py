T =int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())   # N =7 , M=3
    li=[]
    res=[]
    for i in range(N):
        li.append(list(map(int,input().split())))
    # 2차원 배열로 입력 받았고.
    for i in range(N-M+1): # 5번
        for j in range(N-M+1): # i와 j는 가장 왼쪽 상위 좌표.
            sum=0
            for k in range(M):
                for l in range(M):
                    sum+=li[i+k][j+l]
            res.append(sum)

    M = max(res)
    print(f'#{t} {M}')
