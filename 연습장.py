<<<<<<< HEAD
from pprint import pprint

T = int(input())

decode = {
    0: '0001101',
    1: '0011001',
    2: '0010011',
    3: '0111101',
    4: '0100011',
    5: '0110001',
    6: '0101111',
    7: '0111011',
    8: '0110111',
    9: '0001011'
}

for tc in range(1,T+1):
    res = 0
    N, M = map(int,input().split())

    temp = ''
    for _ in range(M):
        temp+='0'

    for i in range(N):
        A = input()
        if A == temp:
            continue
        code = A

    code = list(code)
    while code[-1] == '0':
        code.pop()

    while code[0] == '0':
        code.pop(0)

    code = ''.join(code)

    sparezero = 56 - len(code)
    #print('len',len(code), 'spare',sparezero)
    empty = ''
    for _ in range(sparezero):
        empty += '0'
    code = empty + code
    code2 = []
    for k in range(8):
        temp = code[k*7:(k+1)*7]
        for x in range(10):
            if decode[x] == temp:
                code2.append(x)

    code2 = list(map(int,code2))
    code2 = code2[::-1]

    S = 0

    for i in range(len(code2)):
        if i%2 == 0:
            S += code2[i]

        else:
            S += code2[i]*3

    if S % 10 == 0:
        res = sum(code2)
    print(f'#{tc} {res}')

=======
>>>>>>> fe4413a2bb00a5d00e2deae93e3264b03537a67c
