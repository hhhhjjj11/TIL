# 실3 11659 구간합 

N, M = map(int,input().split()) 

li = list(map(int,input().split())) 

sum = [0] 
sum.append(li[0]) 
#print(sum) 

for i in range(2,N+1):
    sum.append(sum[i-1] + li[i-1])
#print(sum)


for i in range(M):
    L, R = map(int,input().split())
    print(sum[R] - sum[L-1])


