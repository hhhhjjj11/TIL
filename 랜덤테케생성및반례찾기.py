from random import randint
# subprocess.call

# 예제 생성
def example():
    N = randint(2,100)
    graph = []
    for _ in range(N):
        temp = []
        for X in range(N):
            temp.append(randint(1,100))
        graph.append(temp)

    return [N,graph]

# 맞은 답

from collections import deque

def right_sol(n,graph):
    
    maxNum = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > maxNum:
                maxNum = graph[i][j] 
    
    dx = [0 ,0, 1, -1]
    dy = [1, -1, 0 ,0]
    def bfs(a, b, value, visited):
        q = deque()
        q.append((a, b))
        visited[a][b] = 1
    
        while q:
            x, y = q.popleft()
    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > value and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
 
    result = 0
    for i in range(maxNum): 
        visited = [[0] * n for i in range(n)]
        cnt = 0
    
        for j in range(n):
            for k in range(n):
                if graph[j][k] > i and visited[j][k] == 0: 
                    bfs(j, k, i, visited)
                    cnt += 1
    
        if result < cnt:
            result = cnt
    
    return result

# 틀린 답

def wrong_sol(N,city):
    city2 = city[:]
    rain = 0
    cnt = 0

    results = []

    for i in range(1,101):
        rain += 1

        # if cnt == N**2:
        #     #print(i,'에서 끊김')
        #     break
        for r in range(N):
            for c in range(N):
                if 0 < city2[r][c] <= rain:
                    #print('r,c',r,c)
                    city2[r][c] = 0
                    cnt += 1

        #print('rain',rain)
        #print('city')
        #for _ in range(N):
        #    print(city[_])
        # 이제 안전구역 세자
        safe = 0
        check = [[0]*N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if not check[r][c] and city2[r][c] >0:
                    safe+=1
                    deck = deque()
                    deck.append([r,c])
                    while deck:
                        r, c = deck.popleft()
                        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                            if 0<=r+di<N and 0<=c+dj<N and 0 < city2[r+di][c+dj] and not check[r+di][c+dj]:
                                deck.append([r+di,c+dj])
                                check[r+di][c+dj] = 1
        results.append(safe)
        #print('안전지대수',safe)
        #print('check')
        #for _ in range(N):
        #    print(check[_])
    if max(results) == 0: 
        return 1
    else:
        return max(results) 

# 반례 출력
def check():
	ex = example()
	right = right_sol(ex[0], ex[1])
	wrong = wrong_sol(ex[0], ex[1])
	if right != wrong:
		print(ex[0], ex[1])

		print("맞은 답:", right)
		print("틀린 답:", wrong)
		return
	else:
		check()

check()