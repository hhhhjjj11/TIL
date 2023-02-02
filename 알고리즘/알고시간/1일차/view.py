for tc in range(1,11):
    N = int(input()) # 건물 개수
    heights= list(map(int,input().split()))
    
    bds=[]
    for i in range(N):
        li=[0]*255
        for j in range(heights[i]):
            li[j] = 1
        bds.append(li)
    
    cnt=0
    for i in range(2,N-2):
        for j in range(255):
            if bds[i][j] == 0:
                break
            if (bds[i][j] == 1) and (bds[i-2][j]== 0) and (bds[i+2][j] ==0) and (bds[i+1][j]==0) and (bds[i-1][j]==0):
                cnt+=1

    print(f'#{tc} {cnt}')