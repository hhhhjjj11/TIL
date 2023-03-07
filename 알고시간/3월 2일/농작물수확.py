T = int(input())

for tc in range(1, T+1):
    N = int(input())

    garden = [list(map(int,input())) for _ in range(N)]

    K = (N-1)//2

    Adj = set()

    for i in range(K+1):
        for j in range(K+1):
            if i + j <= K:
                Adj.add((i,j))
                Adj.add((-i,j))
                Adj.add((i,-j))
                Adj.add((-i,-j))

    res = 0

    for adj in Adj:
        if 0 <= K + adj[0] < N and 0 <= K + adj[1] < N:
            res += garden[K + adj[0]][K + adj[1]]

    print(f'#{tc} {res}')