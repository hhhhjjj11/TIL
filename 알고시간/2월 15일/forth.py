T = int(input())

op = ['+','-','*','/']

for tc in range(1,T+1):
    li = input().split()
    #print('li',li)

    stack = []

    for s in li:
        if s.isdigit():
            stack.append(s)
        elif s in op:
            try:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
            except:
                res='error'
                break
            #print('연산자',s)
            #print('n1,n2',n1,n2)
            if s == op[0]:
                stack.append(n1+n2)
            elif s == op[1]:
                stack.append(n1-n2)
            elif s == op[2]:
                stack.append(n1*n2)
            elif s == op[3]:
                stack.append(n1//n2)
        elif s == '.':
            if not stack:
                res = 'error'
            else:
                X = str(stack.pop())
                res = (X if X.isdigit() else 'error')

    if stack:
        res = 'error'
    print(f'#{tc} {res}')