def bfs(i, j, N):
    q = [0]*(N*N)
    front = -1
    rear = -1
    visited = [[0]*N for _ in range(N)]
    rear += 1
    q[rear] = (i, j)
    while front != rear:
        front += 1
        i, j = q[front]
        if maze[i][j] == '3':
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!='1' and visited[ni][nj]==0:
                rear += 1
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1
    return 0
 
 
def findStart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                return i, j
    return -1, -1       # return 형식 맞추기용
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
 
    si, sj = findStart(N)
    print(f'#{tc} {bfs(si, sj, N)}')