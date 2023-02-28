from collections import deque

T = int(input())

for tc in range(1,T+1):
    res = 0
    V,E = map(int,input().split())
    g = {}
    for _ in range(E):
        a, b = map(int,input().split())
        if a in g:
            g[a].add(b)
        else:
            g[a]={b}
        if b in g:
            g[b].add(a)
        else:
            g[b]={a}

    S,G = map(int,input().split())

    deck = deque()
    deck.append((S,0,[0]*(V+1)))

    res = 0
    #print('g',g)
    while deck:
        X, cnt, visited = deck.popleft()
        visited[S] = True
        #print('X', X, 'cnt', cnt)
        if X == G:
            res = cnt
            break
        if X in g:
            for i in g[X]:
                if not visited[i]:
                    visited[i] = True
                    deck.append((i,cnt+1,visited))

    print(f'#{tc} {res}')