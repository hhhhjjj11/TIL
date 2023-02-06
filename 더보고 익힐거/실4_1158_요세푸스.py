N, K = map(int,input().split())

li = list(range(1,N+1))

res = []
idx = K-1
while True:
    res.append(li[idx])
    li.remove(li[idx])
    if len(li)==0:
        break
    idx= idx%len(li)
    idx +=K-1
    idx=idx%len(li)
    

for i in range(len(res)):
    res[i]= str(res[i])

print('<'+', '.join(res)+'>')