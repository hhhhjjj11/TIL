N,S = map(int,input().split())

li = list(map(int,input().split()))
cnt= 0 
answers = []
subs =[]
for i in range(1<<N):
    temp=[]
    for j in range(N):
        if i & 1<<j:
            temp.append(li[j])
    if temp:
        subs.append(temp)

for sub in subs:
    if sum(sub) == S:
        cnt+=1

print(cnt)