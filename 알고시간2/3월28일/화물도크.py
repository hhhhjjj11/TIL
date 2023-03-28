T = int(input())

for tc in range(1,T+1):
    res = 0
    N = int(input())
    schedule = []

    for i in range(N):
        A = list(map(int,input().split()))
        schedule.append(A)
    li = list(range(N))

    data = []
    for R in range(N,-1,-1):
        combinations = []
        stack = [([x], i) for i, x in enumerate(li)]    # 첫 값과 각 인덱스를 저장하고

        while stack:
            combination, last_index = stack.pop()

            if len(combination) == R:
                combinations.append(combination)
                continue

            for i in range(last_index+1,len(li)):
                stack.append((combination+[li[i]], i))

        temp = {}
        temp['R'] = R
        temp['combinations'] = combinations
        data.append(temp)

    resolved = False

    for i in range(N,-1,-1):
        for combi in data[N-i]['combinations']:
            BRK = False
            temp = [0]*25
            for j in combi:
                for k in range(schedule[j][0], schedule[j][1]): # 종료시간 -1 까지만, 다음 시작시간과 겹쳐도 상관없게.
                    if temp[k] == 1:
                        BRK = True
                        break
                    else:
                        temp[k] = 1
                if BRK:
                    break
            if BRK:
                continue
            res = i
            # print('res',res)
            # print('combi', combi)
            resolved = True
            break
        if resolved:
            break

    print(f'#{tc} {res}')