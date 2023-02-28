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

    codes = []
    for i in range(N):
        A = input()
        if A == temp:
            continue
        # 0으로만 이루어진 경우가 아니면 2진법으로 바꾸기
        temp2 = []
        for p in range(M):
            x2=A[p]
            num = int(x2,16)
            for j in range(3,-1,-1):
                bit = 1 if num &(1<<j) else 0
                temp2.append(bit)
                #print(bit, end ='')
        if temp2 not in codes:
            codes.append(temp2)

    for x in range(len(codes)):
        code = codes[x]
        #print('code',code)
        temp3 = []
        cnt = 0
        for i in range(len(code)-1,-1,-1):
            if code[i] == 0 and code[i-1] == 1:
                cnt += 1
                temp3.append(cnt)
                cnt = 0
            elif code[i] == 1 and code[i-1] ==0:
                cnt += 1
                temp3.append(cnt)
                cnt = 0
            elif code[i] == 1:
                cnt += 1
            elif code[i] == 0:
                cnt += 1
        temp3.append(0) # 앞에 0개수 모르긴하지만 임의로 0추가해줌 뒤에서 4씩나누기편하게
        temp3 = temp3[::-1]
        codes[x] = temp3
        #print('temp3',temp3)

    #print('codes',codes)

    codebin = []
    for i in range(len(codes)):
        code = codes[i]
        temp1 = []
        temp2 = []
        cnt = 0
        for j in range(len(code)):
            if cnt<32:
                temp1.append(code[j])
                cnt += 1
            elif cnt == 32:
                cnt = 0
                if temp1 not in codebin:
                    codebin.append(temp1)
                temp1 = []
    #print('codebin', codebin)
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
    #print(passwords)
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
        if S % 10 == 0:
            Final += sum(password)

    print(f'#{tc} {Final}')

    # 각각의 0이 아닌 행들에 대하여 오른쪽에서 부터 세준다.

