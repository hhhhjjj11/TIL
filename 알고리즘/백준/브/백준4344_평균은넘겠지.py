T = int(input())
for t in range(T):
    li = list(map(int,input().split()))
    #print('li',li)
    sum=0
    cnt=0
    
    for item in li:
        sum+=item
    sum-=li[0]
    #print('sum',sum,'len',len(li))
    avg=sum/(len(li)-1)
    
    for i in range(1,len(li)):
        if avg<li[i]:
            cnt+=1
    total=len(li)-1
    res=(cnt/total)*100
    res=round(res,3)
    print(f'{res:.3f}%')

    ## 기억하기
    ## round쓰는 경우 정수는 소수점 첫재짜리까지 밖에 표시못함
    ## 이럴 경우 f-string 써야됨 
    ## f'{<숫자>:.<자연수(몇째자리까지표기할지)>f}'