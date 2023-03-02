T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    arrival_time = list(map(int, input().split()))
    arrival_time.sort()
    if arrival_time[0] == 0:
        print(f'#{tc} Impossible')
        continue
    last_time = arrival_time[-1]
    # M 초마다 K 개씩
    t = 0
    fish = 0
    done = False
    for t in range(1, last_time+1):
        if t % M == 0:
            fish += K
        while arrival_time[0] == t:
            fish -= 1
            if fish < 0:
                done = True
                break
            arrival_time.pop(0)
            if not arrival_time:
                done = True
                break
        if done:
            break

    if fish >= 0:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
