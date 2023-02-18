from pprint import pprint

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    snail = []
    for _ in range(N):
        snail.append([0]*N)

    #pprint(snail)

    n = 1

    leng = N

    X = 0

    while True :
        # 가로
        leng = leng
        for i in range(leng):
            if n > N**2:
                break
            snail[0+X][i+X] = n
            n += 1
        
        if n > N**2:
            break

        # 세로
        leng = leng - 1
        for i in range(1,leng+1):
            if n > N**2:
                break
            snail[i+X][N-1-X] = n
            n += 1

        if n > N**2:
            break

        # 가로
        leng = leng
        for i in range(leng):
            if n > N**2:
                break
            snail[N-1-X][N-2-i-X] = n
            n += 1

        if n > N**2:
            break

        # 세로
        leng = leng - 1
        for i in range(leng):
            if n > N**2:
                break
            snail[N-2-i-X][0+X] = n
            n += 1

        if n > N**2:
            break

        # 바퀴추가
        X+=1

    #pprint(snail)
    print(f'#{tc}')
    for A in snail:
        for a in A:
            print(a,end=' ')
        print('')
