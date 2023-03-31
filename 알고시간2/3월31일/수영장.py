T = int(input())

for tc in range(1,T+1):

    fees = list(map(int,input().split()))
    # [하루,한달,세달,1년]
    plan = list(map(int,input().split()))  # 인덱스 + 1 = 월

    # 첫 달 찾기
    for i in range(1,13):
        if plan[i-1]:
            s = i
            break
    li = ['Day','1M','3M']

    stack = [[s, 0]]
    m = 1000000
    while stack:
        # month : 계산할 월, total_fee : month 이전 달 까지 계산한 금액.
        month, total_fee = stack.pop()
        #print(month,total_fee)
        if month > 12:
            if total_fee < m:
                m = total_fee
            continue

        for x in li:
            if x == 'Day':
                what_to_add = plan[month-1]*fees[0]
                stack.append([month+1, total_fee+what_to_add])
            elif x == '1M':
                what_to_add = fees[1]
                stack.append([month+1, total_fee+what_to_add])
            elif x == '3M':
                what_to_add = fees[2]
                stack.append([month+3, total_fee+what_to_add])


    print(f'#{tc} {min(m,fees[3])}')