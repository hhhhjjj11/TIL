# 다익스트라 개념정리 (약간,, bfs,dfs 백트래킹 방법의 일종 같다.)
# - visited를 각 항에 같이 저장하지 않고 지리게 효율적으로 한번에 정하는 방법인듯.

# 최단경로 (혹은 최대경로)를 구하는 알고리즘.
# "최단 거리는 쪼개도 최단거리다"가 성립하는 경우 사용가능한듯.. (아래생각해보기참조)
# 핵심 : 출발점으로부터 현재지점[i]까지 최소경로를 D[i]에 저장한다. 
# 만약 bfs + 덱으로 구현할시,
# 움직였을때 거리가 D[i] 보다 작으면 -> 갱신하고, 다시 덱에 저장.
# D[i] 보다 크거나 같으면 이미 앞에서 따진적있다는 말이므로 덱에 안넣고 버린다.


# 생각해보기
# A 에서 B까지 갈때 A -Y1- X1- Y2 -B로 가는 경로가 가장 빠른 경로이지만
# A 에서 X1까지 가는 경로는 A - Y1 - X1이 가장 빠른 경로가 아닌경우는 다익스트라를 못쓸듯?? 

from collections import deque

T = int(input())

for tc in range(1,T+1):
    N, E = map(int,input().split())

    graph = {}

    for _ in range(E):
        s,e,w = map(int,input().split())
        if s in graph:
            graph[s].add((e,w))
        else:
            graph[s] = {(e,w)}
            
    #print('graph',graph)

    inf = 100000000

    D = [inf]*(N+1)
    D[0] = 0
    # 0에서출발해서 index까지 왔을때 최소거리 저장임
    
    Deck = deque()
    Deck.append(0)

    while Deck:
        now = Deck.popleft()
        if not now in graph:
            continue
        for adj in graph[now]:
            e,w = adj[0],adj[1]
            if D[now] + adj[1] < D[e]:
                D[e] = D[now] + adj[1]
                Deck.append(e)

    print(f'#{tc} {D[N]}')