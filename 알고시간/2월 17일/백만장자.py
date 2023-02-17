T = int(input())

for tc in range(1,T+1):
    N = int(input())

    li = list(map(int,input().split()))

    profit = 0
    if li == sorted(li,reverse=True):
        print(f'#{tc} 0')
        continue
    while li:
        Idx_max = li.index(max(li))
        profit -= sum(li[:Idx_max])
        profit += Idx_max * li[Idx_max]
        li = li[Idx_max+1:]
        #print('li',li)

    print(f'#{tc} {profit}')