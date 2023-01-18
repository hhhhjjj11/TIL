N= int(input())
li = list(map(int,input().split()))

M=max(li)
l=len(li)
sum=0
for i in range(l):
    sum+=100*(li[i]/M)

print(sum/l)