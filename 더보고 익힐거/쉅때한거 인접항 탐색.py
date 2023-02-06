T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    li =[]
    for _ in range(N):
        li.append(list(map(int,input().split())))

    #print('li',li)

    resli = []
    for i in range(N):
        for j in range(M):
            #print(f'{i},{j} 계산시작')
            res = li[i][j]
            d = li[i][j]

            di=[0]*(2*d)
            
            for k in range(1,d+1):
                di.append(k)
                di.append(-k)
            
            dj = list(reversed(di))
            # print('di',di)
            # print('dj',dj)
            for k in range(len(di)):
                ni = i+di[k] 
                nj = j+dj[k]
                if 0 <= ni < N and 0<=nj<M:
                    #print(f'{ni},{nj}',li[ni][nj])
                    res+=li[ni][nj]
            resli.append(res)

    #print(resli)
    #print('len',len(resli))
    print(f'#{tc} {max(resli)}')
        