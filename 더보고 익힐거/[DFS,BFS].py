import sys
from collections import deque

input=sys.stdin.readline

N,M,V = map(int,input().split())

g={}
for i in range(N+1):
    g[i]=set()
for _ in range(M):
    a,b=map(int,input().split())
    g[a].add(b)
    g[b].add(a)

for i in range(1,N+1):
    g[i]=sorted(list(g[i]))

# print(graph)

# print(dic)

visited = [0]*(N+1)
visited[V] = 1
stack = [V]

x = V

# DFS !!

print(V, end=' ')
while True:
    
    B = True
    # if x not in dic.keys():
    #     break

    for i in range(len(g[x])):
        # print(visited)
        # print('x :', x, 'i :',i)
        if not visited[g[x][i]]:
            stack.append(x)
            stack.append(g[x][i])
            print(g[x][i], end=' ')
            visited[g[x][i]] = 1
            B = False
            x = g[x][i]
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

    for i in range(len(g[x])):
        if x in g.keys() and not visited[g[x][i]]:
            deck.append(g[x][i])
            visited[g[x][i]] = 1
