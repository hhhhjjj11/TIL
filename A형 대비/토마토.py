M, N = map(int,input().split())

box = [list(map(int,input().split())) for _ in range(N)]

ik = []
anik = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ik.append((i,j))
        elif box[i][j] == 0:
            anik.append((i,j))

stack = []
t = 0

stack.append((box,ik,t)) # 박스, 익은토마토좌표리스트, 시간

Adj = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우 

res = '?'

if not ik:
    res = -1

elif len(anik) == 0:
    res = 0

if res == '?' :
    while stack:
        box, ik, t = stack.pop()
        #print('박스의상황',box)
        if not ik: # 새롭게 익은 토마토가 없으면 깬다
            break
        temp = []
        for idx in ik:
            i,j =idx[0],idx[1]
            for adj in Adj:
                ni, nj = i+adj[0], j+adj[1]
                if 0<=ni<N and 0<=nj<M and box[ni][nj] == 0:
                    box[ni][nj] = 1
                    temp.append((ni,nj))

        stack.append((box,temp,t+1))
    
    res = t-1
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                res = -1
                break
        if res == -1:
            break

print(res)



