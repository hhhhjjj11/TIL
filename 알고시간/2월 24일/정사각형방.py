from collections import deque

T = int(input())

for tc in range(1,T+1):
    res = 0
    N = int(input())

    room = [list(map(int,input().split())) for _ in range(N)]

    Adj = [(1,0),(-1,0),(0,1),(0,-1)]

    res1 = N**2
    res2 = 0

    for i in range(N):
        for j in range(N):
            deck = deque()
            deck.append([i,j])

            cnt = 1
            while deck:
                ni,nj = deck.popleft()
                for adj in Adj:
                    di, dj = adj
                    if 0 <= ni+di < N and 0 <= nj+dj < N:
                        if room[ni][nj]+1 == room[ni+di][nj+dj]:
                            deck.append([ni+di,nj+dj])
                            cnt += 1
            if res2 < cnt:
                res2 = cnt
                res1 = room[i][j]
            elif res2 == cnt and res1 > room[i][j]:
                res1 = room[i][j]

    print(f'#{tc} {res1} {res2}')