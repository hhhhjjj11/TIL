T = int(input())

for tc in range(1,T+1):
    res = ''

    li = []

    maxlength = 0

    for i in range(5):
        A = input()
        if maxlength < len(A):
            maxlength = len(A)
        li.append(A)

    for i in range(5):
        row = li[i]
        if len(row)<maxlength:
            while len(row)<maxlength:
                row+='.'
        li[i] =row

    #print('li',li)

    for j in range(maxlength):
        for i in range(5):
            if li[i][j] != '.':
                res+=li[i][j]
    print(f'#{tc} {res}')