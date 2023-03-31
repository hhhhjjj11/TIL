T = int(input())

for tc in range(1,T+1):

    fees = list(map(int,input().split()))
    # [하루,한달,세달,1년]
    plan = list(map(int,input().split()))

    # 그렇게 하면 에바같고,, 각 달로 쪼개서 해당 달을 일별로 계산하는게 이득인지 달별로계산하는게 이득인지 계산해보는 식으로 해야할듯.

    # 계산된 달을 체크해야겠다.
    checked = [0]*13  # 인덱스 = 달
    results = []
    total = 0

    for month in range(1,13):
        checked = [0] * 13
        # 해당 달 이용할계획이면, 우선 3달권을 쓸건지부터 계산ㄱ 앞으로 3달간 일,월 계산과 비교
        # 비용 계산한적 없고, 이용 계획 있으면
        if not checked[month] and plan[month-1]:
            print(f'{month}달 계산 시작')
            temp1and2 = 0
            temp3 = fees[2]

            # 일/월로 3달치 계산
            for aa in range(3):
                # 현재달포함 앞으로 3달이 12달이하, 계획에 있으면
                if month + aa <= 12 and plan[month-1+aa]:
                    temp1 = plan[month-1+aa]*fees[0]    # 일계산
                    temp2 = fees[1] # 월계산
                    # 이제 작은값 더해주고
                    temp1and2 += min(temp1, temp2)  # 일, 월 중 더 작은 값을 더해줌.

            # 일+월로 계산한것과 한번에 내는 비용 비교
            if temp3 <= temp1and2:
                total += temp3
            else:
                total += temp1and2

            for aa in range(3):
                if month + aa <= 12:
                    checked[month+aa] = 1

        results.append(total)



    print(f'#{tc} {min(total,fees[3])}')