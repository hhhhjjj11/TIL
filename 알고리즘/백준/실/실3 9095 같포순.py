T = int(input())

def 같포순(a,b,c):
    N = a+b+c
    분자 = 1
    while N>1:
        분자*=N
        N-=1
    분모 = 1
    while a>1:
        분모*=a
        a-=1
    while b>1:
        분모*=b
        b-=1
    while c>1:
        분모*=c
        c-=1
    return 분자//분모


for tc in range(1,T+1):
    total = int(input())
    
    cnt = 0
    # 3의 개수 최대
    M3 = total//3
    #print('M3',M3)
    for i in range(M3+1):  #0 ~ M3
        sub1=total -i*3
        M2 = sub1//2
        for j in range(M2+1): # 0 ~ M2
            개수3,개수2,개수1 = i,j,sub1-2*j
            cnt += 같포순(개수1,개수2,개수3)

    print(cnt)