N = int(input())

li = list(range(1,N+1))

idx = 0 
cnt = 0
res = []
while True:
    if len(res) == N:
        break
    if li[idx]==0:
        idx+=1
        idx=idx%N
    else:
        if cnt%2==0:
            res.append(li[idx])
            #print(f'{idx}항인 {li[idx]}추가')
            #print('res',res)
            cnt+=1
            li[idx]=0
            #print('li',li)
            idx+=1
            idx=idx%N
        else:
            idx+=1
            idx=idx%N
            cnt+=1
            
print(res[-1])
