from pprint import pprint
board = [[2,0,0,2],[0,2,2,2],[2,2,0,2],[2,2,2,2]]
N = len(board[0])

for row in board:
    print(row)

# 합치기 방법1
def move(board, dir):
    if dir == (-1,0): # 위로 움직임
        for j in range(N): # 각 열 별로
            count_zero = 0
            compare = 0
            for i in range(N): # 위에서 한칸씩 아래로 내려오면서 따질거임.
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
                            compare = board[row_of_compare][j]
                            board[i][j] = 0             # 현재값은 0으로 해주고
                            count_zero += 1             # 0카운트 1추가
                        else:                               # 현재랑 비교값이 다르면
                            board[i-count_zero][j] = now    # 옮겨주고
                            board[i][j] = 0                 # 현재자리 0으로
                            compare = now            # 이제 비교 바꿔줘야함
                            row_of_compare = i-count_zero

move(board,(-1,0))

print('board')
for row in board:
    print(row)

# 합치기 방법2 : 스택이용
# 아이디어 : 일단 0 아닌 숫자들 다 덱에 담아놓은 다음, 각 자리에 대하여 덱에서 하나씩 꺼내서 빈자리면 채워넣고 이미 같은값있으면 더하고 다른값있으면 다음자리에 채워넣고..
def move(board, dir):
    pass