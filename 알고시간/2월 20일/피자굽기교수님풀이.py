T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))

    oven = []
    # 화덕 채우기
    for i in range(N):
        oven.append(i)   # 피자번호
    last = N-1
    # 더 이상 피자가 없을 때까지 회전
    ans = 0         # 마지막으로 완성된 피자 번호
    
    # 핵심 : 꺼내보고 다시 넣으면 그만이야 ㅋㅋ
    while oven: 
        num = oven.pop(0)   # 입구로 돌아온 피자 번호
        pizza[num] //= 2    # 한바퀴 돌면서 절반이 녹음
        if pizza[num] > 0:  # 완전히 녹지 않은 경우
            oven.append(num)
        
        # 일단 0인애 계속 받아서 정답으로 재할당 해주면 그만이야 ㅋㅋ
        else:
            ans = num       # 이후에 나오는 피자가 없으면 마지막 피자
            if last + 1< M:      # 아직 화덕에 들어가지 않은 피자가 있으면
                last += 1
                oven.append(last)

    print(f'#{tc} {ans+1}')