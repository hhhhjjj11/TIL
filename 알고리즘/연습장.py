T= int(input())
for t in range(T):
    li = list(map(int,input().split()))
    sum=0
    cnt=0
    
    for item in li:
        sum+=item
    sum-=li[0]
    avg=sum/len(li)
    
    for i in range(1,len(li)):
        if avg<=li[i]:
            cnt+=1
    total=len(li)-1
    res=(cnt/total)*100
    res=round(res,3)
    print(f'{res}%')