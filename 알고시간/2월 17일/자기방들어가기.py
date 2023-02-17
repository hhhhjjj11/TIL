T = int(input())

for tc in range(1,T+1):
    hall = [[0]*200]
    res = 0
    N = int(input())
    li = [list(map(int,input().split())) for _ in range(N)]


    print(f'#{tc} {len(res)}')