

# 내가 푼 풀이.. (다익스트라와 비교해보자)

from collections import deque

T = int(input())

for tc in range(1,T+1):

    N = int(input())

    li = [list(map(int,input().split())) for _ in range(N)]

    #print('li',li)
    # bfs
    Adj = [(0,1),(0,-1),(-1,0),(1,0)]

    deck = deque()
    deck.append([(0,0),0])
    m = 1000000

    visited = [[m]*N for _ in range(N)]

    while deck:
        now, fuel = deck.popleft()
        #print('꺼냄', now,fuel)
        ni,nj = now
        if ni == N-1 and nj == N-1:
            if fuel < m:
                m = fuel
            continue
        for adj in Adj:
            nextI, nextJ = ni+adj[0], nj+adj[1]
            #print('nextI,nextJ',nextI,nextJ)
            if 0 <= nextI < N and 0 <= nextJ < N:
                #print('v',visited)
                height_difference = 0
                if li[nextI][nextJ] > li[ni][nj]:
                    height_difference = li[nextI][nextJ] - li[ni][nj]
                if fuel + height_difference + 1 >= visited[nextI][nextJ]:
                    continue
                else:
                    deck.append([(nextI,nextJ),fuel+1+height_difference])
                    visited[nextI][nextJ] = fuel+1+height_difference

    print(f'#{tc} {m}')