from collections import deque
from pprint import pprint

# 입력받기
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

# 방향 데이터
bh = {'오': (0,1),'왼': (0,-1),'위': (-1,0),'아래':(1,0)}

# 방향바꿔주는 함수
def changedir(d,r):
    if (d =='왼'and r == 'L') or (d == '오' and r == 'D'):
        return '아래'
    elif (d =='왼' and r =='D') or (d == '오' and r == 'L'):
        return '위'
    elif (d == '아래' and r == 'L') or (d== '위' and r == 'D'):
        return  '오'
    elif (d == '아래' and r == 'D') or (d == '위' and r =='L'):
        return '왼'

OVER = False

# 초기방향
dirnow = '오'
di, dj  = bh[dirnow][0], bh[dirnow][1]

tnow = 0

Hi,Hj = 0,0 # 대가리
Ti,Tj = 0,0 # 꼬리

for i in range(L+1):
    if i<L:
        dir = directs[i] 
        time, rot = dir[0], dir[1] # time 이 되면 rot만큼 회전 해야함
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
    dirnow = changedir(dirnow, rot)
    di, dj = bh[dirnow][0], bh[dirnow][1]

res = tnow

print(res)