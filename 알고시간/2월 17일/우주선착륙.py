T = int(input())

for tc in range(1,T+1):
    res = 0

    N, M = map(int,input().split())

    li = [list(map(int,input().split())) for _ in range(N)]

    adj = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,1),(-1,-1)]
    for i in range(N):
        for j in range(M):
            cur_height = li[i][j]
            cnt = 0
            for idx in adj:
                I_adj, J_adj = i+idx[0], j+idx[1]
                if 0<= I_adj <N and 0<= J_adj <M and li[I_adj][J_adj] < cur_height:
                    cnt += 1
                    if cnt == 4:
                        break
            if cnt == 4:
                res += 1

    print(f'#{tc} {res}')