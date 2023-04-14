from collections import deque

n, m = map(int,input())

MAP = [list(map(int,input().split())) for _ in range(n)]


empty = []

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 0:
            empty.append((i,j))

sz = len(empty)

for i in range(sz-2):
    for j in range(i+1,sz-1):
        for k in range(j+1,sz):
            x1, y1 = empty[i]
            x2, y2 = empty[j]
            x3, y3 = empty[k]
            MAP[x1][y1], MAP[x2][y2], MAP[x3][y3] = 1, 1, 1
            
            # bfs..
            deck = deque()

            for p in range(n):
                for q in range(m):
                    if MAP[p][q] == 2:
                        deck.append((p,q))
            
            while deck:
                ni,nj = deck.popleft()
                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if 0<=ni+di<n and 0<= nj+dj<m:
                        
            
            MAP[x1][y1], MAP[x2][y2], MAP[x3][y3] = 0, 0, 0
