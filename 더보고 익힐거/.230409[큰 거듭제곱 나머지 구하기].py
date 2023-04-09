# 해보기 B를줄여가기


# 이렇게 하는것보다는 B를 반씩 줄여나가는 편이 깔끔하다.
# 일단 해보자.

A,B,C = map(int,input().split())

if B == 1:
    print(A%C)

else:

    n = 2

    DP= [A%C] # DP[i] = A의 2^idx승의 나머지
    rest = A%C

    while True:
        rest = (rest **2) % C   # B가 1이면 여기서 문제 생김. 걍 A%C가 정답인데 변질됨. 
        DP.append(rest)
        if n*2 > B :
            break
        n *= 2

    # 남은 곱해야할 횟수 = B - n
    B -= n

    # print( '남은곱해야할수', B)
    # print('dp',DP)

    cursor = len(DP)-1

    while B>0:
        cursor -=1
        while 2**cursor > B:
            cursor -= 1
        
        # print('cursor',cursor, '뺄숫자', 2**cursor)
        B-=2**cursor
        rest = (rest * DP[cursor])%C
        # print('현재까지 계산한 나머지', rest)
        # print('남은 곱할 횟수',B)


    print(rest)