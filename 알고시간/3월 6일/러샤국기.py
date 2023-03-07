T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]

    m = N*M

    for cut1 in range(1, N-1):
        for cut2 in range(cut1+1, N):
            cnt = 0
            # 영역1에서는 'W'가아닌 칸의 갯수
            for i in range(cut1):
                for j in range(M):
                    if flag[i][j] != 'W':
                        cnt += 1
            for i in range(cut1,cut2):
                for j in range(M):
                    if flag[i][j] != 'B':
                        cnt += 1
            for i in range(cut2,N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        cnt += 1
            if cnt < m:
                m = cnt
            # print('cut1,cut2,cnt',cut1,cut2,cnt)
    print(f'#{tc} {m}')

