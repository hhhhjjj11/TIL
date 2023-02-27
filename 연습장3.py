from pprint import pprint
board = [[2,0,0],[0,2,2],[2,2,0]]
N =3
for row in board:
    print(row)

def move(board, dir):
    if dir == (-1,0): # 위로 움직임
        for j in range(N):
            count_zero = 0
            compare = 0
            for i in range(N):
                now = board[i][j]
                if now == 0:
                    count_zero += 1
                else:        # 0 이 아니면
                    if not compare:     # 비교값이 없으면
                        compare = now   # 처음으로 0이아닌 값을 compare로 설정.
                        if count_zero:
                            board[i-count_zero][j] = now
                            board[i][j] = 0
                        row_of_compare = i-count_zero
                    else:                       # 비교값이 있을때
                        if now == compare:              # 현재랑 비교값이 같으면
                            board[row_of_compare][j] *= 2    # 비교값을 두배해주고 
                            board[i][j] = 0             # 현재값은 0으로 해주고
                            count_zero += 1             # 0카운트 1추가
                        else:                               # 현재랑 비교값이 다르면
                            board[i-count_zero][j] = now    # 옮겨주고
                            board[i][j] = 0                 # 현재자리 0으로
                            copare = now            # 이제 비교 바꿔줘야함
                            row_of_compare = i

move(board,(-1,0))

print('board')
for row in board:
    print(row)