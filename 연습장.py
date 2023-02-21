# 정리
# 미로찾기에서 해답이존재하는지 여부만 알고싶은경우는 걍 DFS가 빠를듯
# 근데 최소경로를 찾는경우에는 bfs가 나은가 봄?
# 왜냐하면 dfs로 찾으려면 모든 경로 다 뒤진다음 젤 짧은값 비교해야하는데
# bfs로가면 그냥 도착하면 끝내면 되니까

from collections import deque

T = int(input())

for tc in range(1,T+1):
    res = 0
    N = int(input())

    maze = [list(map(int,input())) for i in range(N)]

    for i in range(N):  
        for j in range(N):
            V = maze[i][j]
            if V == 2:
                Si,Sj = i,j
            elif V == 3:
                Fi,Fj = i,j
    
    deck = deque()
    
    print(f'#{tc} {res}')