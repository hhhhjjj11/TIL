N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def move(ni,nj,di,dj):
    cnt = 0
    while 0< ni < N-1 and 0< nj < N-1:
        ni -= di
        nj -= dj
        cnt += 1
    return ni,nj,cnt

visited = {}
s = [board]

while s:
    bd = s.pop()
    for dir in direction:
        if dir[0] != 0:     # 위아래로 움직이는 경우임. 이 경우 가로줄끼리 계산
            for i in range(N):
                for j in range(N):
                    ni, nj, ncnt = move(i,j,dir[0],dir[1])
        else:   # 좌우로 움직이는 경우임. 이 경우 세로줄 계산
            pass
def move(board, dir):
    if dir == (-1,0): # 위로 움직임
        for j in range(N):
            temp = 0
            for i in range(N):
                if board[i][j] == 0:
                    temp += 1
                elif board[i][j] != 0:
                    if i<N and board[i][j] == board[i+1][j] :
                        if temp != 0:
                            board[i-temp][j] = board[i][j]*2
                        else:
                            board[i][j] *=2
                            board[i+1][j] = 0





    return board


stack = [board]

while stack:
    bd = stack.pop()

