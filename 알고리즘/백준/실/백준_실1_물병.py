from sys import stdin

# T = int(stdin.readline())
# for t in range(T):
#     a, b = map(int,stdin.readline().split())


N, K =map(int,stdin.readline().split())
li=[N]
   
# 각 항에 대하여,
# 2의몫 을 다음 항으로 보내고 
# 2의 나머지를 남긴다.

cnt=0
while True:
    for i in range(len(li)):
        if i==(len(li)-1):
            li.append(0)
        if li[i]>1:    
            li[i+1]+=li[i]//2
            li[i]=li[i]%2

        if sum(li)<=K:
            break
    #print(li)
    if sum(li)<=K:
        break
    else:
        li[0]+=1
        cnt+=1
    #    print(li)
    
if cnt==0:
    print(-1)
else:
    print(cnt)



#######################################

import sys

n, k = map(int, input().split())

count = 0

while bin(n).count('1') > k:
    n = n+1
    count = count +1

print(count)