T = int(input())
memo = {}

for tc in range(1,T+1):
    cnt_max = 0
    N, M = map(int,input().split())
    city = [list(map(int,input().split())) for _ in range(N)]
    results=[]
    for i in range(N):
        for j in range(N):
            K = 1
            while True:
                if K == N+2:
                    break
                cnt_home = 0
                if K not in memo:
                    temp = set()
                    for p in range(K):
                        for q in range(K):
                            if p+q <= K-1:
                                temp.add((p, q))
                                temp.add((-p,q))
                                temp.add((p,-q))
                                temp.add((-p,-q))
                    temp = list(temp)
                    memo[K] = temp
                for adj in memo[K]:
                    di,dj = adj
                    if 0 <= i+di < N and 0 <= j+dj < N and city[i+di][j+dj] == 1:
                        cnt_home += 1
                        #print('cnt',cnt_home)
                cost = K**2 + (K-1)**2
                profit = M * cnt_home
                res = profit - cost

                if res >= 0 and cnt_max < cnt_home:
                    #print('i,j,K,cost,profit,res,cnt',i,j,K,cost,profit,res,cnt_home)
                    cnt_max = cnt_home

                K += 1

    print(f'#{tc} {cnt_max}')