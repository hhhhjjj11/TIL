from collections import deque

N = int(input())

g = [list(map(int,input().split())) for _ in range(N)]

# 노드 : 0 ~ N-1 번

Ans = [[0]*N for _ in range(N)]

# bfs
visited = []
for i in range(N):
    for j in range(N):
        if i not in visited:
            deck = deque()
            deck.append(i)

            while deck:
                node_now = deck.popleft()
                
                for node_next in range(N):
                    if node_now == node_next:
                        continue
                    if g[node_now][node_next]: # 길이 있으면
                        pass

        visited.append(i)


# 아이디어
# 