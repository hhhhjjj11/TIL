T = int(input())

for tc in range(1, T+1):

    res = 0
    N = int(input())
    li = []
    for _ in range(N):
        li.append(list(map(int,input().split())))

    #print('li',li)
    p = list(range(N))

    stack = [([value], [index]) for index, value in enumerate(p)]

    Answer = []

    while stack:
        per, idx = stack.pop()

        if len(per) == len(p):
            Answer.append(per)

        for i in range(len(p)):
            if not i in idx:
                stack.append((per + [p[i]], idx + [i]))

    #print(Answer)
    m = 1000000
    for perm in Answer:
        temp = 0
        for k in range(N):
            temp += li[k][perm[k]]
            if temp > m:
                break
        if temp <= m:
            m = temp

    print(f'#{tc} {m}')