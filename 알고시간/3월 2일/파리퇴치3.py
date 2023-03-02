T = int(input())

Adj1 = [(1,0),(-1,0),(0,1),(0,-1)]
Adj2 = [(1,1),(-1,-1),(1,-1),(-1,1)]

def spray1(i,j,M):
    res = li[i][j]
    for k in range(1,M):
        for adj in Adj1:
            I_adj, J_adj = i+adj[0]*k,j+adj[1]*k
            if 0<=I_adj<N and 0<=J_adj<N:
                res += li[I_adj][J_adj]
    return res

def spray2(i,j,M):
    res = li[i][j]
    for k in range(1,M):
        for adj in Adj2:
            I_adj, J_adj = i+adj[0]*k,j+adj[1]*k
            if 0<=I_adj<N and 0<=J_adj<N:
                res += li[I_adj][J_adj]
    return res


for tc in range(1,T+1):
    N, M = map(int,input().split())
    li = [list(map(int,input().split())) for _ in range(N)]

    Max = 0
    for i in range(N):
        for j in range(N):
            if Max < spray1(i,j,M):
                Max = spray1(i,j,M)
            if Max < spray2(i,j,M):
                Max = spray2(i,j,M)

    print(f'#{tc} {Max}')