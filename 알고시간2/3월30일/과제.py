T = int(input())

for tc in range(1,T+1):
    N = int(input())
    li = []
    for _ in range(N):
        temp = list(map(int,input().split()))
        temp = list(map(lambda x: x/100, temp))
        li.append(temp)

    res = 0

    p = list(range(N))

    stack = [[[x], li[0][x]] for x in p]

    M = 0
    while stack:
        perm, prob= stack.pop()

        if len(perm) == len(li):
            if prob > M :
                M = prob
        else:
            for i in p:
                if i not in perm:
                    if prob * li[len(perm)][i] <= M :
                        continue
                    else:
                        stack.append((perm+[i], prob * li[len(perm)][i]))

    print(f'#{tc}',end=' ')
    print("{:.6f}".format(M*100))