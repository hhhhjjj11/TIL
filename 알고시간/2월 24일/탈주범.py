from pprint import pprint
from collections import deque

T = int(input())

dir = {
    1: [(1,0,{1,2,4,7}),(0,1,{1,3,6,7}),(0,-1,{1,3,4,5}),(-1,0,{1,2,5,6})], # 하 우 좌 상
    2: [(1,0,{1,2,4,7}),(-1,0,{1,2,5,6})],  # 상 하
    3: [(0,1,{1,3,6,7}),(0,-1,{1,3,4,5})],  # 좌 우
    4: [(-1,0,{1,2,5,6}),(0,1,{1,3,6,7})],  # 상 우
    5: [(1,0,{1,2,4,7}),(0,1,{1,3,6,7})],   # 하 우
    6: [(1,0,{1,2,4,7}),(0,-1,{1,3,4,5})],  # 하 좌
    7: [(-1,0,{1,2,5,6}),(0,-1,{1,3,4,5})]  # 상 좌
}

for tc in range(1,T+1):

    res = 1
    N, M, R, C, L = map(int,input().split())
    
    TR = [list(map(int,input().split())) for _ in range(N)]

    deck = deque()
    deck.append((R,C,1))
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1

    while deck:
        ni, nj, nt = deck.popleft()
  
        if nt < L:
            if TR[ni][nj] in dir:

                for direction in dir[TR[ni][nj]]:
                    di, dj, possible = direction
                    if 0<=ni+di<N and 0<=nj+dj<M and not visited[ni+di][nj+dj] and TR[ni+di][nj+dj] in possible:
                        res += 1
                        visited[ni+di][nj+dj] = 1
                        deck.append((ni+di,nj+dj, nt+1))

    print(f'#{tc} {res}')

