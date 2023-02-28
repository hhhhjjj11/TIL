for tc in range(1,11):
    test_num , N = map(int,input().split())
    inp = list(map(int,input().split()))
    graph = {}
    for i in range(N):
        s,g = inp[2*i],inp[2*i+1]
        if s in graph:
            graph[s].add(g)
        else:
            graph[s] = {g}
    #print(graph)
    visited = [False]*100

    now = 0
    visited[now] = True

    stack = [now]

    while stack:

        x = stack.pop()

        if x in graph:
            for node in graph[x]:
                if not visited[node]:
                    stack.append(x)
                    stack.append(node)
                    visited[node] = True
                    break

    #print('visited',visited)
    res = (1 if visited[99] else 0)
    print(f'#{tc} {res}')