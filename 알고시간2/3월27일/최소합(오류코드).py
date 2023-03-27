def permf(i,k): # i: 값을 결정할 자리, k: 결정할 개수
    if i==k:
        # print(*p)
        perms.append([*p])
    else:
        for j in range(i, k): # 자신부터 오른쪽 원소들과 교환
            p[i],p[j] = p[j],p[i]
            permf(i+1,k)
            p[i],p[j] = p[j],p[i]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    li = [list(map(int,input().split())) for _ in range(N)]
    p=''
    for _ in range(N-1):
        p+='1'
        p+='2'

    perms = []
    permf(0, 2*(N-1))
    #print('perms',perms)
    m = 100000000

    set(perms)

    for perm in perms:
        isbreak = False
        ni, nj = 0,0
        temp = 0
        temp += li[ni][nj]
        for dir in perm:
            if dir=="R":
                adj = [0,1]
            else:
                adj = [1,0]
            nexti, nextj = ni + adj[0], nj + adj[1]
            print('좌표',nexti,nextj)
            if 0<= nexti <N and 0<=nextj<N:
                temp += li[nexti][nextj]
                ni, nj = nexti, nextj
            else:
                isbreak = True
                break
        if isbreak:
            continue

        if temp < m:
            m = temp

    print(f'#{tc} {m}')