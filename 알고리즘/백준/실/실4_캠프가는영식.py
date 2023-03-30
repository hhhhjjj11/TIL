N, T = map(int,input().split())

informs =[]
for _ in range(N):
    S,L,C = map(int,input().split())
    informs.append((S,L,C))

    # 만약에 버스운영시간에 걸리지 않으면:
    # 1. 시간대가 맞는 애들을 고른다음에
    # 2. 만약에 빈배열이면 버스 못타는거니까 -1 출력

temp = []
waitings = []

for inform in informs:
    S,L,C = inform
    if S + L*(C-1) < T:
        continue
    temp.append((S,L,C))
if not temp:
    print(-1)
else:
    resolved = False
    while temp:
        S,L,C = temp.pop()
        # 만약에 버스 운영시간 전에 도착했으면 -> 시작할때 까지만 기다리면 됨
        if T < S:
            waitings.append(S-T)
        # 시작시간 지나고 언제 도착했으면..
        else:
            # 만약에 정각에 도착했으면 -> 따질것도 없음 걍 0찍고 끝내면 됨.
            for i in range(C):
                if S + L*i == T:
                    print(0)
                    resolved = True
                    break
            if resolved:
                break
            # 정각에 안걸리면
            else:
                # 사이에 걸리는 애들 부터 찾은다음 가장 가까운 큰 값까지 빼서 임시저장.
                for j in range(1,C):
                    if S + L*(j-1) < T < S+L*j:
                        waitings.append(S + L*j - T)
                        break

    if not resolved:
        print(min(waitings))

