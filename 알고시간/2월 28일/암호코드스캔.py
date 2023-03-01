import sys
sys.stdin = open('13.txt', 'r')

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
    print('len',len(codes))
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
    print('개수 39여야함',len(codebin))
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
        print('S',S)
        print('i, S, sum', i, S, sum(password))
        if S % 10 == 0:
            Final += sum(password)

    print(f'#{tc} {Final}')

    # 각각의 0이 아닌 행들에 대하여 오른쪽에서 부터 세준다.