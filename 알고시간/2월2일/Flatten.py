for tc in range(1,11):
    chance = int(input())
    chance2 = chance
    li = list(map(int,input().split()))

    cntli  = [0]*100   # 인덱스 + 1 = 층 수

    for item in li:
        for i in range(item):
            cntli[i]+=1
    
    #print(cntli)
    # #큰값에서 dmps만큼 빼기
    for i in range(99,-1,-1): # 99 98 97 96 ...
        if chance==0:
            break
        while cntli[i]>0:
            if chance==0:
                break
            cntli[i]-=1
            chance-=1
    
    #print(cntli)        
    #작은값에서 dmps 만큼 더하기 
    for i in range(100):
        if chance2==0:
            break
        while cntli[i]<100:
            if chance2==0:
                break
            cntli[i]+=1
            chance2-=1

    # cntli에서 100이아닌 가장 작은 인덱스 와 0이아닌 가장큰 인덱스를 구해서 빼면 됨.
    maxIdx = 0
    for i in range(99,-1,-1):
        if cntli[i] != 0:
            maxIdx=i
            break
    #print('max',maxIdx)
    minIdx = 0
    for i in range(100):
        if cntli[i] != 100:
            minIdx = i
            break
    #print('min',minIdx)

    res = maxIdx-minIdx
    print(f'#{tc} {res+1}')
