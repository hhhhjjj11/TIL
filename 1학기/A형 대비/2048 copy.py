N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

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
