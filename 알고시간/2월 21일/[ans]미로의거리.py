def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)] # 인큐 확인배열
    q = [(i,j)]             # 큐 생성, 시작점 인큐
    visited[i][j] = 1       # 시작점 표시
    while q:                # 큐가 비어있지 않으면
        i, j = q.pop(0)
        if maze[i][j]=='3': # i,j가 도착지인가?
            return visited[i][j] - 2
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!='1' and visited[ni][nj]==0: # 벽이 아니고, 인큐한 적 없으면
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0        # '3'칸에 못가는 경우
 
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
 
    # si = sj = -1
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j]=='2':
    #             si, sj = i, j
    #             break
    #     if si!=-1:
    #         break
    si, sj = findStart(N)
 
    print(f'#{tc} {bfs(si, sj, N)}')