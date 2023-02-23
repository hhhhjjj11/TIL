n, m = map(int,input().split())
MAP = []
for _ in range(n):
    MAP.append(list(map(str,input())))

# 일단 겹치고 이런거 신경쓰지말고 cnt만세놓고 이동시키는 함수 간단하게 작성한다음에
# 함수 실행 결과가지고 어찌저찌 해결할거야. 
# move함수자체는 간단함.

def move(x,y,dx,dy):
    cnt = 0
    nx, ny = x, y

    while MAP[nx+dx][ny+dy] != '#' and MAP[nx+dx][ny+dy] != 'O':
        nx += dx
        ny += dy
        cnt += 1
    return nx, ny, cnt

for r in range(n):
    for c in range(m):
        if MAP[r][c] == 'R':
            rsx, rsy = r, c
        if MAP[r][c] == 'B':
            bsx, bxy = r, c
        if MAP[r][c] == 'O':
            ox, oy = r, c

def solution():
    visited = {} 
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    visited[(rsx,rsy)] = 1
    s = [[rsx,rsy,bsx,bsy,0]]       
        
