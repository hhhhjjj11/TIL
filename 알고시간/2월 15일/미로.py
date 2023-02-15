from pprint import pprint

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,list(input()))) for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if maze[i][j] == 3:
                Sx,Sy = i,j
            elif maze[i][j] == 2:
                Fx,Fy = i,j

    stack = []
    stack.append((Sx,Sy))

    visited = [[False]*N for _ in range(N)]
    visited[Sx][Sy] = True

    adj = [(1,0),(-1,0),(0,1),(0,-1)]

    while stack:
        x,y = stack.pop()

        for idx in adj:
            i, j = x+idx[0],y+idx[1]
            if 0<= i < N and 0 <= j < N:
                if not visited[i][j] and maze[i][j] in (0,2):
                    stack.append((x,y))
                    stack.append((i,j))
                    visited[i][j] = True
                    break

    res = 1 if visited[Fx][Fy] else 0
    print(f'#{tc} {res}')