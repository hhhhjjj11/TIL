T = int(input())
Adj = [(1,0),(0,1)]

for tc in range(1,T+1):
    N = int(input())
    li = [list(map(int,input().split())) for _ in range(N)]

    m = 1000000

    stack = []

    stack.append((0,0,li[0][0]))

    while stack:
        ni,nj,S = stack.pop()
        if ni == N-1 and nj == N-1:
            if S < m:
                m = S
            else:
                continue
        for adj in Adj:
            nexti = ni + adj[0]
            nextj = nj + adj[1]
            if 0 <= nexti < N and 0 <= nextj < N:
                S_next = S + li[nexti][nextj]
                if S_next > m:
                    continue
                stack.append((nexti,nextj,S_next))

    print(f'#{tc} {m}')