T = int(input())

for tc in range(1,T+1):
    P,A,B = map(int,input().split())

    li = list(range(P+1))

    L = 1
    R = P   

    cntA=0
    cntB=0

    while R>=L:
        M=(L+R) // 2
        if M == A:
            break
        elif M<A:
            L = M
            cntA+=1
        else:
            R = M
            cntA+=1

    L=1
    R=P
    
    while R>=L:
        M=(L+R) // 2
        if M == B:
            break
        elif M<B:
            L = M
            cntB+=1
        else:
            R = M
            cntB+=1

    if cntA > cntB:
        print(f'#{tc} B')
    if cntA < cntB:
        print(f'#{tc} A')
    if cntA == cntB:
        print(f'#{tc} 0')