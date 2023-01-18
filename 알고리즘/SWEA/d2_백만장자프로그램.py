T = int(input())
for t in range(1,T+1):
    N=int(input())
    li=list(map(int,input().split()))  # [1,1,3,1,2]
    new_li=sorted(li)  # [1,1,1,2,3]
    res=0
    if li==sorted(li,reverse=True):
        print(f'#{t} 0')
    else:
        while len(li)>0:
            Max=max(li) # 3        
            M_index=li.index(Max)  # 2번째
            for i in range(M_index):
                res-=li[i]
            res+=Max*(M_index) # res=4

            # 배열 뒷부분 
            li=li[M_index+1:] # [1,2]
        print(f'#{t} {res}')

