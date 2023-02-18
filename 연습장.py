T = int(input())

for tc in range(1,T+1):
    res = 0
    N = int(input())
    li = (list(map(int,input().split())) for i in range(N))

    for i in range(N):
        res = []
        
 
    print(f'#{tc} {res}')


# 방문표시하는 식으로하면 안됨 왜냐하면 방문표시 취소해야함