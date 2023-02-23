n, m = map(int,input().split())
MAP = []
for _ in range(n):
    MAP.append(list(map(str,input())))

# 기울이는 동작을 해주는 함수를 ! 좌표뿐만아니라 방향도 함께 인자로 받아서
# 방향에 관계없이 사용할 수 있도록 만들어준다는점.
# 이때 움직이는 이동량을 체크하기 위해 각함수가 실행될때마다 움직이는 칸 수를 기록해두고,
# 파란공이랑 빨간공이 겹치는 상황에 활용한다!!!


def move(x, y, dx, dy):
    cnt = 0
    nx, ny = x, y
    while MAP[nx + dx][ny + dy] != '#' and MAP[nx][ny] != 'O':
        nx += dx
        ny += dy
        cnt += 1
    return nx,  ny, cnt

# 시작위치 저장
for r in range(n):
    for c in range(m):
        if MAP[r][c] == 'R':
            # red starting x, y
            rsx, rsy = r, c
        if MAP[r][c] == 'B':
            # blue starting x, y
            bsx, bsy = r, c
        if MAP[r][c] == 'O':
            # hole x, y
            ox, oy = r, c

# print(MAP)

def solution():
    visited = {}     # visited 를 dic 으로 저장한다... 차원제한 X. 여러 다른 형식들을 저장하기에 편리하다.
    moves = [(-1,0),(1,0),(0,-1),(0,1)] # 방향벡터..
    s = [[rsx,rsy,bsx,bsy,0]] # 스택에 현재 상태 저장

    while s:
        rx, ry, bx, by, cnt = s.pop(0) 
        if cnt >= 10: # 백트레킹.. cnt가 10보다 커지면 탐색 멈춤.
            return -1 

        for dx, dy in moves: # 현재 위치에서 한번씩 움직여볼거임                   
            rrx, rry, rcnt = move(rx,ry,dx,dy) # 빨간공 움직이고
            bbx, bby, bcnt = move(bx,by,dx,dy) # 파란공 움직인다.

            if MAP[bbx][bby] != 'O':            # 파란공이 구멍에 안들어갔을 때.
                if rrx == ox and rry == oy:     # 빨강공이 구멍에 들어갔으면
                    return cnt + 1              # 현재까지에 1을 더한다음 리턴.
                
                # 빨간공이랑 파란공이 겹치는 것을 이런식으로 해결한다는 점 알고 있기.
                if rrx == bbx and rry == bby:   # 만약에 파란공이랑 빨간공이랑 같으면
                    #더 늦게 도착한놈을 한칸 뒤로 뺌
                    if rcnt > bcnt:          
                        rrx, rry = rrx-dx, rry-dy 
                    else:
                        bbx, bby = bbx-dx, bby-dy

                if (rrx,rry,bbx,bby) in visited:    # 이미 방문했었던 곳이면 다른방향으로 기울여보기
                    continue
                else:                               # 이런상황은 처음이면
                    visited[(rrx,rry,bbx,bby)] = 1  # 현재 공들 위치 저장하고
                    s.append([rrx,rry,bbx,bby,cnt+1])   # 현재 공들의 위치와 cnt를 스택에 저장..
                    # print("방문처리 : ", rrx, rry, bbx, bby, cnt+1)

    return -1

print(solution())