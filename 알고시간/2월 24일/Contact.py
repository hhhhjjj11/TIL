from collections import deque

for tc in range(1,11):
    length, start = map(int,input().split())
    li = list(map(int,input().split()))

    g = {}

    for i in range(length//2):
        a, b = li[i*2], li[i*2+1]
        if a in g:
            g[a].add(b)
        else:
            g[a] = {b}

    deck = deque([(start,0)])
    visited = [0]*101
    li_dist = [0]*101

    while deck:
        X, distance = deck.popleft()
        li_dist[X] = distance

        if X in g:
            for node in g[X]:
                if not visited[node]:
                    deck.append((node,distance+1))
                    visited[node] = 1

    M = max(li_dist)
    Max_idxes = []
    for idx, dist in enumerate(li_dist):
        if dist == M:
            Max_idxes.append(idx)

    print(f'#{tc} {max(Max_idxes)}')