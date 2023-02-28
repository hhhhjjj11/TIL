T = int(input())

for tc in range(1,T+1):
    hall = [0]*200
    N = int(input())
    li = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        m = min((li[i][0]-1)//2, (li[i][1]-1)//2)
        M = max((li[i][0]-1)//2, (li[i][1]-1)//2)
        for j in range(m,M+1):
            hall[j] += 1
    
    print(f'#{tc} {max(hall)}')
