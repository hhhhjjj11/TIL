from collections import deque

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    deck = deque([[N,0]])
    YS = list(range(4))
    res = 0
    resolved = False
    checked= [0]*1000001
    while deck:
        num, cnt = deck.popleft()
        for ys in YS:
            if ys == 0 and 1<=num+1<=1000000 and not checked[num+1]:
                if num+1 == M:
                    res = cnt+1
                    resolved =True
                    break
                else:
                    deck.append([num+1,cnt+1])
                    checked[num+1] = 1
            elif ys == 1 and 1<=num-1<=1000000 and not checked[num-1]:
                if num-1 == M:
                    res = cnt+1
                    resolved = True
                else:
                    deck.append([num-1,cnt+1])
                    checked[num-1] = 1
            elif ys == 2 and 1<=num*2<=1000000 and not checked[num*2]:
                if num*2 == M:
                    res = cnt +1
                    resolved = True
                else:
                    deck.append([num*2,cnt+1])
                    checked[num*2] =1
            elif ys ==3 and 1<=num-10 <=1000000 and not checked[num-10]:
                if num-10 ==M:
                    res = cnt+1
                    resolved= True
                else:
                    deck.append([num-10, cnt + 1])
                    checked[num-10] =1
        if resolved:
            break
    print(f'#{tc} {res}')
