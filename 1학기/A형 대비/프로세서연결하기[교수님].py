di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def connect(n, d, N):
    i, j = processor[n][0], processor[n][1]
    ni, nj = i + di[d], j + dj[d]
    while 0<=ni<N and 0<=nj<N and arr[ni][nj]==0 and used[ni][nj]==0:
        ni, nj = ni + di[d], nj + dj[d]
    cnt = 0
    if ni<0 or ni>=N or nj<0 or nj>=N:
        ni, nj = i + di[d], j + dj[d]
        while 0 <= ni < N and 0 <= nj < N:
            used[ni][nj] = 1
            cnt += 1
            ni, nj = ni + di[d], nj + dj[d]
    return cnt


def disconnect(n, d, N):
    i, j = processor[n][0], processor[n][1]
    ni, nj = i + di[d], j + dj[d]
    while 0 <= ni < N and 0 <= nj < N:
        used[ni][nj] = 0
        ni, nj = ni + di[d], nj + dj[d]

def f(i, K, p, s, N):     # i 연결할 프로세서 번호, k연결할 개수, p연결된 개수, s전선 길이, N크기
    global minV
    global maxP
    if i == K:
        if maxP < p:            # 더 많은 프로세서가 연결되면
            maxP = p
            minV = s
        elif maxP == p:         # 연결된 개수가 같으면
            minV = min(minV, s)
    elif maxP > p+K-i:
        return
    else:
        for d in range(4):
            dir[i] = d
            l = connect(i, d, N)
            t = 1 if l > 0 else 0
            f(i + 1, K, p + t, s + l, N)
            if t:
                disconnect(i, d, N)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*N for _ in range(N)]
    processor = []
    for i in range(1, N-1):     # 가장자리 제외
        for j in range(1, N-1):
            if arr[i][j]:
                processor.append((i, j))
    K = len(processor)
    dir = [0]*K
    minV = 1000000
    maxP = 0
    f(0, K, 0, 0, N)
    print(f'#{tc} {minV}')