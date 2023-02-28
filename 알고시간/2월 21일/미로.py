from collections import deque

T = int(input())

for tc in range(1,T+1):

    res = 0
    N = int(input())

    maze = [list(map(int,input())) for i in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                Si,Sj = i,j
            elif maze[i][j] == 3:
                Fi,Fj = i,j

    Adj = [(1,0),(-1,0),(0,1),(0,-1)] # 아래 위 우 좌

    deck = deque()
    deck.append((Si,Sj,0,[[False]*N for i in range(N)]))

    m = N**2
    Proper= False
    while deck:
        curI,curJ,cnt, visited = deck.popleft()
        visited[Si][Sj] = True
        for I_adj in Adj:
            nextI,nextJ = curI + I_adj[0], curJ + I_adj[1]
            if 0 <= nextI < N and 0 <= nextJ < N:
                if maze[nextI][nextJ] == 3:
                    Proper = True
                    if cnt <= m:
                        m = cnt
                elif maze[nextI][nextJ] == 0 and not visited[nextI][nextJ]:
                    #print(nextI,nextJ,'로 이동')
                    cnt += 1
                    #print('cnt',cnt)
                    if cnt <= m:
                        visited[nextI][nextJ] = True
                        deck.append((nextI,nextJ,cnt,visited))
                        #print('deck',deck)
                    cnt -=1

    if Proper:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')