T = int(input())

for tc in range(1,T+1):
    K,N,M = map(int,input().split())   # K3 N10 M5
    charge = list(map(int,input().split()))  # 1,3,5,7,9

    now = 0
    cnt=0
    
    while True:
        isPossible = 0
        
        if now +K>=N:
            isPossible=1
            break
        if now + K in charge:
            now = now + K
            #print('now',now, 'cnt',cnt)
            isPossible=1
            cnt+=1
        else:
            for i in range(now+K-1, now, -1):
                if i in charge:
                    now = i
                    #print('now',now, 'cnt',cnt)
                    isPossible=1
                    cnt+=1
                    break
        if isPossible==0:
            cnt = 0
            break

    print(f'#{tc} {cnt}')