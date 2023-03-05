from collections import deque

N = int(input())
K = int(input())

board = [[0]*N for _ in range(N)]
board[0][0] = 'S'

for i in range(K):
    a, b = map(int,input().split())
    board[a-1][b-1] = 'A'

snk = deque()
snk.append((0,0))

L = int(input())

directs=[]
for i in range(L):
    a, b = input().split()
    a = int(a)
    directs.append((a,b))

dir = [(-1,0), (0,1), (1,0), (0,-1)] 
# 시계방향.. 위 오른쪽 아래 왼쪽 인덱스기준 +1 하면 오른쪽으로 회전, -1하면 왼쪽으로 회전함.

OVER = False

# 초기방향
dnow = 1
di, dj  = dir[dnow][0],dir[dnow][1]

tnow = 0

Hi,Hj = 0,0 # 대가리

for i in range(L+1):
    if i<L:
        direct = directs[i] 
        time, rot = direct[0], direct[1] # time 이 되면 rot만큼 회전 해야함
    while True:
        tnow+=1
        # 머리 이동(현재방향으로)
        Hi += di
        Hj += dj
        # 벽에 박으면
        if not (0<= Hi <N and 0<= Hj <N):
            OVER =True
            break
        # 만약 사과를 만나면
        if board[Hi][Hj] == 'A':
            board[Hi][Hj] = 'S'
            snk.append((Hi,Hj)) # 덱에 좌표저장
        # 빈공간이면
        elif board[Hi][Hj] == 0:
            board[Hi][Hj] = 'S'
            snk.append((Hi,Hj))
            Ti, Tj = snk.popleft()
            board[Ti][Tj] = 0
        # 지몸에 갖다 박으면
        elif board[Hi][Hj] == 'S':
            OVER = True
            break     
        if tnow == time : 
           break       
    
    if OVER:
        break
    # tnow == time 이되면 방향 바꾸기 (while문 빠져나왓으니.)
    if rot == 'D':
        dnow = (dnow+1)%4
    elif rot == 'L':
        dnow = (dnow-1)%4
    di, dj = dir[dnow][0], dir[dnow][1]

res = tnow

print(res)