T = int(input())

for tc in range(1,T+1):
    jinsoo2 = list(input())
    jinsoo3 = list(input())

    N2 = len(jinsoo2)
    N3 = len(jinsoo3)

    #print('N2',N2, 'N3',N3)
    res = 0

    temp2before10 = []
    temp3before10 = []

    for j in range(N2):
        if jinsoo2[j] == '1':
            jinsoo2[j] = '0'
            temp2before10.append(jinsoo2[:])
            # print('1',temp2before10)
            # 원래대로 돌려주기
            jinsoo2[j] = '1'
        else:
            jinsoo2[j] = '1'
            temp2before10.append(jinsoo2[:])
            # print('0', temp2before10)
            # 원래대로 돌려주기
            jinsoo2[j] = '0'

    tempnums = ['0', '1', '2']

    for j in range(N3):
        numnow = jinsoo3[j]
        for candidate in tempnums:
            # 숫자바꿔보고 10진수로바꾼다음에 temp3에 추가
            if numnow != candidate:
                jinsoo3[j] = candidate
                # 10진수 변환
                temp3before10.append(jinsoo3[:])
                # 다시 원래대로
                jinsoo3[j] = numnow

    #print('tem3before',temp3before10)
    # 이제 각 temp의 원소들을 10진수로 변환
    temp2 = []
    temp3 = []

    for i in range(len(temp2before10)):
        li_in_2 = ''.join(temp2before10[i])
        pass
        # join으로 합쳐주고 10진수 변환 후 append
        # print('li_in_2',li_in_2)
        temp2.append(int(f'0b{li_in_2}', 2))

    #print('temp2',temp2)

    for i in range(len(temp3before10)):
        li_in_3 = ''.join(temp3before10[i])
        pass
        # join으로 합쳐주고 10진수 변환 후 append
        temp3.append(int(f'{li_in_3}', 3))

    resolved = False
    for i in temp2:
        for j in temp3:
            if i == j:
                res = i
                resolved = True
                break
        if resolved:
            break

    print(f'#{tc} {res}')