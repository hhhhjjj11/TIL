T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())  # V : 노드의 개수, E : 간선 개수

    graph = {}

    for _ in range(E):
        s,g = map(int,input().split())
        if s in graph:
            graph[s].add(g)
        else:
            graph[s] = {g}
    
    S,G  = map(int,input().split())

    visited = [False]*(V+1)

    now = S
    visited[now] = True

    stack = []
    stack.append(now)

    while stack:
        
        x = stack.pop()

        if x in graph:
            for node in graph[x]:
                if not visited[node]:
                    stack.append(x)
                    stack.append(node)
                    visited[node] = True
                    break

    if visited[G] :
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')