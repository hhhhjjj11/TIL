T=int(input())    # ABACABACA   //GAGARRGAGARR 
for t in range(1,T+1):  
    res=0
    li=list(input())  # [A,B,A,C,A,B,A,C]  //
    for i in range(1, len(li)+1): # 항개수만큼반복, 1부터시작
        isRight=1
        if li[0]==li[i]:   #첫번째항이랑비교  
            res=i             #걸리면 일단 할당, 2
            for j in range(i):  # for j in range(2), j=0,1
                if li[j] != li[j+i]: #전부확인, li[0] = li[2] , li[1]=li[3]
                    isRight=0
            if isRight==1:
                break
    print(f'#{t} {res}')


    ## 주의 확인스위치 리셋을 포문 안에서 해줘야함!!! ##