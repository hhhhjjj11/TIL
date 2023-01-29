n = int(input())
res = []
for _ in range(n):
    j,m = map(int,input().split())
    r = (j-1)%(m+1)
    #print(r)
    ans =2*((j-1-r)//(m+1))+2  # 
    res.append(ans)

#print(res)
M= min(res)
index= res.index(M)
print(index+1,M)