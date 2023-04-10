from collections import deque

while True:
    w, h = map(int,input().split())
    if (w,h) == (0,0):
        break
    MAP = []
    for _ in range(h):
        MAP.append(list(map(int,input().split())))

    check = [[0]*w for _ in range(h)]

    #print('MAP',MAP)

    cnt = 0 
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1 and not check[i][j]:
                cnt += 1
                deck = deque()
                deck.append((i,j))

                while deck:
                    ni,nj = deck.popleft()

                    for di,dj in [(1,0),(-1,0),(1,1),(-1,-1),(0,1),(0,-1),(-1,1),(1,-1)]:
                        if 0 <= ni + di < h and 0<= nj + dj < w and MAP[ni+di][nj+dj] == 1 and not check[ni+di][nj+dj]:
                            deck.append((ni+di,nj+dj))
                            check[ni+di][nj+dj] = 1
                
    print(cnt)
