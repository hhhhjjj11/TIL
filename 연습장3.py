N=int(input())
d={}
d[1]=3
d[2]=7
d[3]=17
for n in range(4,N+1):
    d[n]=(d[n-2]*5+d[n-3]*2)%9901
print(d[N])