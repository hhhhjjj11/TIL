from collections import deque

N,M,V = map(int,input().split())

li = []
for i in range(M):
    li.append(list(map(int,input().split())))

visited = [0] * (N+1)
d = deque()
d.append(V)

while d:
    x= d.popleft()
    
    if x == 

