C = int(input())

n = int(input())

li = {}

for _ in range(n):
    a, b = map(int,input().split())
    if a in li:
        li[a].add(b)
    else:
        li[a] = {b}
    if b in li:
        li[b].add(a)
    else:
        li[b] = {a}

visited = [False]*(C+1)

now = 1
visited[now] = True

for i in li:
    li[i] = sorted(li[i])

#print(li)

stack=[1]

cnt = 0

while stack :

    x = stack.pop()
    
    if x in li:
        for node in li[x]:
            if not visited[node]:
                stack.append(x)
                stack.append(node)
                visited[node] = True
                cnt+=1
                break

print(cnt)

