import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

visit = [[False]*8 for _ in range(8)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(board):
    que = deque([])

    # 바이러스 있는 공간을 확인하려고....
    
    # 초기화
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 2):
                que.append((i, j))
                visit[i][j] = True
            else:
                visit[i][j] = False
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            n_x, n_y = x+ dx[i], y + dy[i]  #인접 좌표
            if (not visit[i][j] and board[i][j] != 1) and (0 <= n_x < len(board) and 0 <= n_y < len(board[0])):
                que.append((n_x, n_y))
                visit[n_x][n_y] = True
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if visit[i][j]:
                cnt += 1
    return cnt
def solve(board):
    g = [] # 벽이 없는 공간
    for x in range(n):
        for y in range(m):
            if board[x][y] != 1:
                g.append((x, y))
    sz = len(g)
    res = 0
    for i in range(sz -2):
        for j in range(i+1,sz -1):
            for k in range(j+1, sz):
                x1, y1 = g[i]
                x2, y2 = g[j]
                x3, y3 = g[k]
                board[x1][y1], board[x2][y2], board[x3][y3] = 1, 1, 1
                res = max(res, bfs(board))
                board[x1][y1], board[x2][y2], board[x3][y3] = 0, 0, 0
    return res
board = [list(map(int, input().split())) for i in range(n)]
print(solve(board))

# 뭔가를 해봤을 때 bfs탐색을 해본다

# 벽을 세워보고 
# 각각의 벽에 대해 
# bfs실행
# 벽을 다시 없애기


def solve(board):
    g = [] # 벽이 없는 공간
    for x in range(n):
        for y in range(m):
            if board[x][y] != 1:
                g.append((x, y))
    sz = len(g)
    res = 0
    for i in range(sz -2):
        for j in range(i+1,sz -1):
            for k in range(j+1, sz):
                x1, y1 = g[i]
                x2, y2 = g[j]
                x3, y3 = g[k]
                board[x1][y1], board[x2][y2], board[x3][y3] = 1, 1, 1
                
                visit

                board[x1][y1], board[x2][y2], board[x3][y3] = 0, 0, 0
    return res