

# MST (최소신장트리)
# 일단 bfs,dfs로는 왜 안되는지 제껴두고, 
# 구하는 방법 두가지 있음 : Prim, Kruskal
# 둘다 별로 안어렵고, 크게 복잡하지도 않음. 

# Prim으로 풀어보자.
# 아이디어...
# -> 
# 일단 현재 트리에 만든 노드들을 MST에 저장한다. (처음엔 시작점 0만 들어있다.) (말하자면 결과 트리로 확정한 노드들을 담는다.)
# 확정된 노드들의 인접노드들 중에서 가장 작은 가중치를 갖는 노드를 찾아서 MST에 담는다.
# MST에 모두 담길때까지 반복한다. 
# 이런식으로 하면 원하는 답을 얻을 수 있다. 증명은 생략한다...

T = int(input())

for tc in range(1,T+1):
    res = 0
    V, E = map(int,input().split())

    graph  = {}

    for _ in range(E):
        s,e,w = map(int,input().split())
        if s in graph:
            graph[s].add((e,w))
        else:
            graph[s] = {(e,w)}
        if e in graph:
            graph[e].add((s,w))
        else:
            graph[e] = {(s,w)}

    MST = set()     
    MST.add(0)
    ans = 0

    while len(MST) != V+1 :
    #for _ in range(V):
        m  = 1000000 
        for node in MST:
            for adj in graph[node]:
                e,w = adj
                if e not in MST:
                    if w < m:
                        m = w
                        m_node = e
        MST.add(m_node)
        ans += m

    print(f'#{tc} {ans}')
