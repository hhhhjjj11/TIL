T = int(input())

for tc in range(1,T+1):
    res = 1

    E,N = map(int,input().split())
    li = list(map(int,input().split()))
    li2 = [0] * (E+2)
    for i in range(E):
        P, S = li[2*i],li[2*i + 1]
        li2[S] = P

    level_now = [N]
    while True:
        if not level_now:
            break
        level_next=[]
        for n in level_now:
            for i in range(len(li2)):
                if n == li2[i]:
                    level_next.append(i)
                    res += 1
        level_now = level_next[:]

    print(f'#{tc} {res}')