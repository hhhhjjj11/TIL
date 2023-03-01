# import sys
# sys.stdin = open('1242_in.txt', 'r')

T = int(input())

decode = {
    0: '3211',
    1: '2221',
    2: '2122',
    3: '1411',
    4: '1132',
    5: '1231',
    6: '1114',
    7: '1312',
    8: '1213',
    9: '3112'
}

for tc in range(1,T+1):
    res= 0
    N, M = map(int,input().split())

    temp = ''

    for _ in range(M):
        temp += '0'

    # 0으로만 이루어진 항을 제외하고 입력 받는다.
    input_not_zero = []
    length_of_input = 0
    for i in range(N):
        A = input()
        if A == temp:
            continue
        input_not_zero.append(A)
        length_of_input += 1

    #print(input_not_zero)

    # 2진법으로 바꿔준다.
    input_2jin =[]
    for i in range(length_of_input):
        row = input_not_zero[i]
        temp = []
        for j in range(M):
            num = int(row[j],16)
            for k in range(3,-1,-1):
                bit = 1 if num & (1<<k) else 0
                temp.append(bit)
        input_2jin.append(temp)

    # print(input_2jin)
    # print('len', len(input_not_zero),len(input_2jin))

    # 이제 직사각형배열을 입력 받아야한다. 어덯게?
    # 여기서. 주어진 조건을 활용해야함.
    # 주어진 코드들은 모두 1로끝난다. 또 0으로 시작한다.. 그런데 모든 암호들은 0으로 구분된다..
    # 배경과 시작이 모두 0이므로, 어디부터 시작하는지 알기 어렵다..
    # 암호코드는 길수도 있지만, 1231 -> 2462처럼 0과 1의 반복횟수를 배하는 방식으로만 길어진다.
    # 따라서 "횟수를 세어 나타낸 것의 길이"는 변하지않는다. 그것은 항상 32개이다. 8자리, 각 자리의 값이 얼만지 나타내는 4개의숫자 
    # 횟수를 세어나타낸 것과 횟수세기전 인덱스를 동시에 다뤄줘야함.
    # 따라서 뒤에서부터 세서 1이 나온 곳 부터 1의 갯수와 0의 갯수를 차례로 세어서, 31번째까지 숫자가 바뀌는 곳을 찾는다. 맨 앞에 0이 몇개로 시작하는지는 세지 않는다. 
    # 이를 통해 첫 1과 마지막 1의 인덱스를 저장한다.  
    # 다음 행에서 해당 부분이 같으면 넘어가고 

    codes = [] # 직사각형 배열의 첫 줄을 담을 빈배열

    for i in range(length_of_input): # 뒤에서부터 왼쪽으로 탐색
        row = input_2jin[i]
        cnt = -1
        for j in range(len(row)-1,-1,-1):
            if cnt<0 and row[j] == 1 : # 처음으로 1나오면 cnt 0만듬. (세기시작) 
                cnt += 1
                Fi = j
            if cnt >= 0 and row[j] != row[j-1]: # 세기시작하고나서 0에서1 또는 1에서0으로 바뀔때마다 cnt 1씩증가
                cnt += 1
            if cnt == 31: # 현재 인덱스가 마지막1의 인덱스임.
                Si = j
                compare = row[Si:Fi+1]
                codes.append(compare)
                #print('APPEND!!', codes)
                for k in range(i+1, length_of_input): # 다음행들에 대해 같은것들을 싹다 찾아서 0으로바꿔.
                    nextrow = input_2jin[k]
                    if nextrow[Si:Fi+1] == compare : # 다음행의 같은위치에 똑같이 생겨먹었다면(직사각형배열이라면)
                        for l in range(Si,Fi+1):
                            nextrow[l] = 0 # 0으로 바꿔준다.
                    else:               # 다음행이 직사각형 배열 아니면 break.
                        break
                cnt = -1 # 초기화

    # print('#############################')
    # print('codes',codes)
    # print('#############################')

    # 이제 모든 줄을 0의 개수와 1의 개수를 세서 바꿔준다. 
    for i in range(length_of_input):
        row = input_2jin[i]


    for x in range(len(codes)):
        code = codes[x]
        while code[-1] ==0:
            code.pop()
        while code[0] == 0:
            code.pop(0)
        #print('code',code)
        temp3 = []
        cnt = 0
        for i in range(len(code)-1,-1,-1):
            if i != 0:
                if code[i] != code[i-1]:
                    cnt += 1
                    temp3.append(cnt)
                    cnt = 0
                else:
                    cnt+=1
            else:
                cnt+=1
                temp3.append(cnt)
        temp3.append(0) # 앞에 0개수 모르긴하지만 임의로 0추가해줌 뒤에서 4씩나누기편하게
        temp3 = temp3[::-1]
        codes[x] = temp3
        #print('len',len(codes[x]))
        #print('temp3',temp3)

    #print('codes',codes)
    #print('len',len(codes))
    codebin = []
    for i in range(len(codes)):
        code = codes[i]
        temp1 = []
        cnt = 0
        for j in range(32):
            if cnt < 32:
                temp1.append(code[j])
                cnt += 1
            if cnt == 32:
                cnt = 0
                #print('tmep1',temp1)
                if temp1 not in codebin:
                    codebin.append(temp1)
                temp1 = []
    #print('codebin', codebin)
    #print('개수 39여야함',len(codebin))
    for i in range(len(codebin)):
        code = codebin[i]
        sortedcode = sorted(code)
        m = sortedcode[1]
        if m != 1:
            codebin[i] = list(map(lambda x: x//m,code))

    passwords = []

    for i in range(len(codebin)):
        code = codebin[i]
        code = list(map(str,code))
        code = ''.join(code)
        password = []
        for j in range(8):
            X = code[j * 4:(j + 1) * 4]
            if j == 0:
                X = X[1:]
                for k in range(10):
                    if decode[k][1:] == X:
                        password.append(k)
                pass # 뒤에 세개만 비교해야함
            else:
                for k in range(10):
                    if decode[k] == X:
                        password.append(k)
        if len(password) == 8:
            passwords.append(password)

    
    Final = 0
    for i in range(len(passwords)):
        password = passwords[i]
        password = password[::-1]
        #print('password',password)
        S = password[0]
        for j in range(1,len(password)):
            if j%2 == 0:
                S += password[j]
            else:
                S += password[j]*3
        #print('S',S)
        #print('i, S, sum', i, S, sum(password))
        if S % 10 == 0:
            Final += sum(password)

    print(f'#{tc} {Final}')

    # 각각의 0이 아닌 행들에 대하여 오른쪽에서 부터 세준다.