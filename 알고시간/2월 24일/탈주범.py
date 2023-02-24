from collections import deque

T = int(input())

dir = {
    1: [(1,0),(0,1),(0,-1),(-1,0)],
    2: [(1,0),(-1,0)],
    3: [(0,1),(0,-1)],
    4: [(-1,0),(0,1)],
    5: [(1,0),(0,1)],
    6: [(1,0),(0,-1)],
    7: [(-1,0),(0,-1)]
}

for tc in range(1,T+1):
    res = 1
    N, M, R, C, L = map(int,input().split())

    TR = [list(map(int,input().split())) for _ in range(N)]
    #print('TR',TR)
    deck = deque()
    time = 1
    deck.append((R,C,time))
    visited = [[0]*(M)]*N
    #print('visited',visited)

    while deck:
        ni, nj, nt = deck.popleft()
        if nt == L:
            break
        if TR[ni][nj] in dir:
            #print('TR',TR[ni][nj])
            for direction in dir[TR[ni][nj]]:
                #print('direction',direction)
                di, dj = direction
                if 0<=ni+di<N and 0<=nj+dj<M and not visited[ni+di][nj+dj] and TR[ni+di][nj+dj] !=0:
                    res += 1
                    visited[ni+di][nj+dj] = 1
                    deck.append((ni+di,nj+dj, nt+1))

    print(f'#{tc} {res}')