from collections import deque

T = int(input())


for tc in range(1,T+1):
    checked = [0] * 1000001
    N, M = map(int,input().split())
    deck = deque()
    deck.append([N,0])
    res = 0

    while deck:
        num, cnt = deck.popleft()
        #print('꺼냄',num,cnt)
        if num == M:
            res = cnt
            break
        if 0<num<=1000000 and not checked[num]:
            deck.append([num+1,cnt+1])
            deck.append([num-1,cnt+1])
            deck.append([num*2,cnt+1])
            deck.append([num-10,cnt+1])
            checked[num] = 1

    print(f'#{tc} {res}')
