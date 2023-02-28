N = 16
for _ in range(10):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                Si,Sj = i,j
            elif maze[i][j] ==3:
                Fi,Fj = i,j

    Adj = [(1,0),(-1,0),(0,1),(0,-1)]
    res = 0
    stack = []
    stack.append((Si,Sj))
    while stack:
        x,y = stack.pop()
        #print('현재위치',x,y)
        for idx in Adj:
            i, j = x+idx[0], y+idx[1]
            if 0<= i<N and 0 <=j <N:
                if not visited[i][j]:
                    if maze[i][j] == 0:
                        stack.append((x,y))
                        stack.append((i,j))
                        visited[i][j] = True
                        break
                    elif maze[i][j] == 3:
                        res=1
                        break
        if res:
            break
    if not res:
        res = (1 if visited[Fi][Fj] else 0)
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} {res}')