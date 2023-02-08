N,M,V = map(int,input().split())

graph = []
for i in range(M):
    graph.append(list(map(int,input().split())))

dic ={}
for item in graph:
    dic[item[0]] = dic.get(item[0],{item[1]})
    dic[item[0]].add(item[1])

for key, value in dic.items():
    dic[key] = list(dic[key])

print(graph)
print(dic)

visited = [0]*(N+1)
visited[V] = 1 
stack = [V]
res = [V]

while stack:

    x = stack.pop()

    for i in range(len(dic[x])):
        if not visited[dic[x][i]]:
            stack.append(dic[x][i])
            