from collections import deque

N,M,V = map(int,input().split())

graph = []
for i in range(M):
    graph.append(list(map(int,input().split())))

dic ={}
for item in graph:
    dic[item[0]] = dic.get(item[0],{item[1]})
    dic[item[0]].add(item[1])
    dic[item[1]] = dic.get(item[1],{item[0]})
    dic[item[1]].add(item[0])

for key, value in dic.items():
    dic[key] = sorted(list(dic[key]))


# print(graph)

#print(dic)

visited = [0]*(N+1)
visited[V] = 1
stack = [V]
res = [V]

x = V

# DFS !!

print(V, end=' ')
while True:

    B = True
    # if x not in dic.keys():
    #     break

    for i in range(len(dic[x])):
        # print(visited)
        # print('x :', x, 'i :',i)
        if not visited[dic[x][i]]:
            stack.append(x)
            stack.append(dic[x][i])
            print(dic[x][i], end=' ')
            visited[dic[x][i]] = 1
            B = False
            x = dic[x][i]
            break

    if len(stack) == 0:
        break

    if B == True:
        x = stack.pop()

print('')

# 이제 BFS 해보자 !!
visited = [0]*(N+1)
visited[V] = 1

deck = deque()
deck.append(V)
res = []

while deck:

    x = deck.popleft()
    print(x, end=' ')

    # if x not in dic.keys():
    #     break

    for i in range(len(dic[x])):
        if x in dic.keys() and not visited[dic[x][i]]:
            deck.append(dic[x][i])  
            visited[dic[x][i]] = 1