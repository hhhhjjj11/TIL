T = int(input())

def garo(i,j):
    res = 0
    #print('가로실행 i,j',i,j)
    if board[i][j:j+5] =='ooooo':
        #print(board[i][j:j+5])
        res = 1
    return res

def sero(i,j):
    res = 1
    for k in range(i,i+5):
        if board[k][j] != 'o':
            res = 0
    return res

def daegak1(i,j):
    res = 1
    for k in range(5):
        if board[i+k][j+k] != 'o':
            res = 0
    return res

def daegak2(i,j):
    res = 1
    for k in range(5):
        if board[i+k][j-k] != 'o':
            res = 0
    return res



for tc in range(1,T+1):
    res = 0
    N = int(input())
    board = [input() for _ in range(N)]
    #print('board',board)
    res = 0
    for i in range(N):
        for j in range(N-4):
            #print('가로')
            if garo(i,j):
                res = 1
    for i in range(N-4):
        for j in range(N):
            if sero(i,j):
                res = 1
    for i in range(N-4):
        for j in range(N-4):
            #print('i,j',i,j)
            #print('가세대')
            if daegak1(i,j):
                res = 1
    for i in range(N-4):
        for j in range(N-1,3,-1):
            if daegak2(i,j):
                res = 1
    res = 'YES' if res else 'NO'
    print(f'#{tc} {res}')