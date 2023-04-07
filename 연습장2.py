from collections import deque

N = int(input())

city = [list(map(int,input().split())) for _ in range(N)]
rain = 0
cnt = 0

results = []

for i in range(1,101):

    if cnt == N**2:
        #print(i,'에서 끊김')
        break
    for r in range(N):
        for c in range(N):
            if 0 < city[r][c] <= rain:
                #print('r,c',r,c)
                # 물에잠긴부분 0으로처리
                city[r][c] = 0
                cnt += 1

    #print('rain',rain)
    print('city')
    for _ in range(N):
        print(city[_])
    # 이제 안전구역 세자
    safe = 0
    check = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 처리한적이 없고 침수되지 않은지역이면
            if not check[r][c] and city[r][c] > 0:
                safe+=1
                deck = deque()
                deck.append([r,c])
                check[r][c]=1
                while deck:
                    r, c = deck.popleft()
                    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        # 행과 열이 범위 안에 있고 침수지역이 아니고 체크한적이 없으면
                        if 0<=r+di<N and 0<=c+dj<N and 0 < city[r+di][c+dj] and not check[r+di][c+dj]:
                            deck.append([r+di,c+dj])
                            check[r+di][c+dj] = 1
    print('safe',safe)
    results.append(safe)
    #print('안전지대수',safe)
    #print('check')
    #for _ in range(N):
    #    print(check[_])
    rain += 1

if max(results) == 0: 
    print(1)
else:
    print(max(results)) 