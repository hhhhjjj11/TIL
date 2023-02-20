from collections import deque

T = int(input())
for tc in range(1,T+1):
    N ,M = map(int,input().split())
    li = list(map(int,input().split()))
    cheese = deque([[value,index] for index,value in enumerate(li)])
    fire = deque()

    if N>=M:
        fire = cheese
        while len(cheese) >1:
            i = -1
            while True:
                i += 1
                if i >= len(fire) or len(fire) ==1:
                    break
                cheese[i][0] //= 2
                if cheese[i][0] == 0:
                    cheese.remove([cheese[i][0],cheese[i][1]])
                    i -= 1
        last_pizza = cheese[0][1] + 1

    else:
        while len(fire) < N:
            fire.append(cheese.popleft())
        while len(fire)>1:
            i = -1
            while True:
                i += 1
                if i >= len(fire) or len(fire) ==1:
                    break
                fire[i][0] //= 2
                if fire[i][0] == 0:
                    if cheese:
                        fire[i] = cheese.popleft()
                    elif not cheese:
                        fire.remove([fire[i][0],fire[i][1]])
                        i -= 1

        last_pizza = fire[0][1]+1

    print(f'#{tc} {last_pizza}')

