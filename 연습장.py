from collections import deque

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

deck = deque()

deck.append((board, 0))

direction = [(1,0),(0,1),(-1,0),(0,-1)]

def move(board, dir):
    if dir == (1,0): # 아래로 -> 각 열 별로 따져야함.
        for j in range(N):
            deck2 = deque()
            for i in range(N-1,-1,-1):
                if board[i][j] != 0:
                    deck2.append(board[i][j])
                    board[i][j] = 0
            ni, nj = N-1, j
            while deck2:
                x = deck2.popleft()
                if not board[ni][nj]: # 0이면 걍 넣고
                    board[ni][nj] = x
                elif board[ni][nj] ==  x: # 뭐 있는데 같으면 더하고
                    board[ni][nj] *= 2
                    ni -= 1 # 커서 위로 한칸 올리고
                else: # 뭐 있는데 다르다. -> 커서 한칸 올리고 거따가 넣는다.
                    ni -= 1
                    board[ni][nj] = x
    elif dir == (-1,0):
        for j in range(N):
            deck2 =deque()
            for i in range(N):
                if board[i][j] != 0:
                    pass
    elif dir == (0,1):
        pass
    elif dir == (0,-1):
        pass

    return board

M = 0

while deck:
    board, cnt = deck.pop(0)
    if cnt > 5:
        break
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if board[i][j] > M:
                    M = board[i][j]
    for dir in direction:
        board_after_move = move(board, dir)
        deck.append(board_after_move, cnt+1)

print(M)

