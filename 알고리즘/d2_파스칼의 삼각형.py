T = int(input())
for t in range(1,T+1):
    N=int(input())
    if N==2:
        print(f'#{t}')
        print(1)
        print(1, 1)
    if N==1:
        print(f'#{t}')
        print(1)
    if N>=3:
        li=[[1],[1,1]]    
        for i in range(3,N+1):
            add=[0]*i   # lets say N=5, then, At the first, i=3, add=[0,0,0]
            add[0]=add[-1]=1   # add=[1,0,1]
            for j in range(1,i-1):  #range(1,2) -> j=1
                add[j]=li[i-2][j]+li[i-2][j-1]   # add[1]=li[1][1]+li[1][0]
                # add=[1,2,1]
            li.append(add) # li=[[1],[1,1],[1,2,1]]
        print(f'#{t}')
        for i in range(N):
            for num in li[i]:
                print(num, end=' ')
            print('')

