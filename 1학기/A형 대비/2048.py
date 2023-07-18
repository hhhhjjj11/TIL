# 정리1. 일단 입력받을때 이제 sys.stdin으로 받아야함. 입력받을거 많으니까 차이 많이난다.
# 정리2. 크게크게 덩어리 끼리 해결방법 생각해서 큰그림 그려놓고 함수 구현


from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

deck = deque()
deck.append((board, 0))

direction = [(1,0),(-1,0),(0,-1),(0,1)]

def move(board, dir):
    # 인풋을 건들지 않고 움직인 다음 배열을 반환하기 위하여 deepcopy해준다는 점..
    board_copy = [board[i][:] for i in range(len(board))]

    if dir == (1,0): # 아래로 -> 각 열 별로 따져야함.
        for j in range(N):
            deck2 = deque()
            for i in range(N-1,-1,-1):
                if board_copy[i][j] != 0:
                    deck2.append(board_copy[i][j])
                    board_copy[i][j] = 0
            ni, nj = N-1, j
            while deck2:
                x = deck2.popleft()
                if not board_copy[ni][nj]: # 0이면 걍 넣고
                    board_copy[ni][nj] = x
                elif board_copy[ni][nj] ==  x: # 뭐 있는데 같으면 더하고
                    board_copy[ni][nj] *= 2
                    ni -= 1 # 커서 위로 한칸 올리고
                else: # 뭐 있는데 다르다. -> 커서 한칸 올리고 거따가 넣는다.
                    ni -= 1
                    board_copy[ni][nj] = x
    elif dir == (-1,0): # 위로
        for j in range(N):
            deck2 =deque()
            for i in range(N):
                if board_copy[i][j] != 0:
                    deck2.append(board_copy[i][j])
                    board_copy[i][j] = 0
            ni, nj = 0, j
            while deck2:
                x = deck2.popleft()
                if not board_copy[ni][nj]:
                    board_copy[ni][nj] = x
                elif board_copy[ni][nj] == x:
                    board_copy[ni][nj] *= 2
                    ni += 1
                else:
                    ni += 1
                    board_copy[ni][nj] = x
    elif dir == (0,1): # 오른쪽으로
        for i in range(N):
            deck2 = deque()
            for j in range(N-1,-1,-1):
                if board_copy[i][j] != 0:
                    deck2.append(board_copy[i][j])
                    board_copy[i][j] = 0
            ni, nj = i, N-1
            while deck2:
                x = deck2.popleft()
                if not board_copy[ni][nj]:
                    board_copy[ni][nj] = x
                elif board_copy[ni][nj] == x:
                    board_copy[ni][nj] *= 2
                    nj -= 1
                else:
                    nj -= 1
                    board_copy[ni][nj] = x
    elif dir == (0,-1): # 왼쪽
        for i in range(N):
            deck2 = deque()
            for j in range(N):
                if board_copy[i][j] != 0:
                    deck2.append(board_copy[i][j])
                    board_copy[i][j] = 0
            ni, nj = i, 0
            while deck2:
                x = deck2.popleft()
                if not board_copy[ni][nj]:
                    board_copy[ni][nj] = x
                elif board_copy[ni][nj] == x:
                    board_copy[ni][nj] *= 2
                    nj += 1
                else:
                    nj += 1
                    board_copy[ni][nj] = x

    board_after_move = board_copy
    return board_after_move

M = 0
# visited = []
# visited.append(board)

while deck:
    board, cnt = deck.popleft()
    if cnt > 5:
        break

    for i in range(N):
        for j in range(N):
            if board[i][j] > M:
                M = board[i][j]
    else:
        for direct in direction:
            board_after_move = move(board, direct)
            # if board_after_move not in visited:
            deck.append((board_after_move, cnt+1))
            # visited.append(board_after_move)

print(M)