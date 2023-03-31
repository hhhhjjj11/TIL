T = int(input())

for tc in range(1,T+1):
    res = 0
    N, B = map(int,input().split())

    H = list(map(int,input().split()))

    # 조합을이용한다. 조합 + 백트래킹
    index_list = list(range(N))

    stack = [[[x], H[x]] for x in index_list]

    m = 200000
    while stack:
        combs, total = stack.pop()
        # 전부다 합쳤다?
        if B <= total < m:
            m = total
        # 조합수집하기
        else:
            for i in range(combs[-1]+1, N):
                if i not in combs:
                    # 가지치기
                    if total+H[i] > m:
                        continue
                    else:
                        stack.append([combs+[i], total+H[i]])

    print(f'#{tc} {m-B}')