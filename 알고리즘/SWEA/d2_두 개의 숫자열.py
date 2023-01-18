T = int(input())
for t in range(1, T+1):
    N,M=map(int,input().split())
    li1=list(map(int,input().split()))
    li2=list(map(int,input().split()))
    reslist=[]
    if N<=M :
        for i in range(M-N+1):
            s=0
            for j in range(N):
                s+=li1[j]*li2[j+i]
       
            reslist.append(s)
    else :
        for i in range(N-M+1):
            s=0
            for j in range(M):
                s+=li2[j]*li1[j+i]
            reslist.append(s)
    m=max(reslist)
    print(f'#{t} {m}')
        