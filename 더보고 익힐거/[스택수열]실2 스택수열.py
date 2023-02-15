n = int(input())

stack = []
li = [int(input()) for i in range(n)]
#print('li',li)
wanted = []
op = []
what_to_append = 1
res = 'OK'
for num in li:
    #print('다음항계산시작', num)
    if stack:
        if stack[-1] == num:
            x = stack.pop()
            #print('pop',stack)
            op.append('-')
            wanted.append(x)
            continue
        elif stack[-1] > num:
            while True:
                x = stack.pop()
                op.append('-')
                if x == num:
                    wanted.append(x)
                    break
                if not stack:
                    res= 'NO'
                    break
        elif stack[-1] < num:
            while True:
                stack.append(what_to_append)
                op.append('+')
                if what_to_append == num:
                    x = stack.pop()
                    op.append('-')
                    wanted.append(x)
                    what_to_append+=1
                    break
                what_to_append += 1
                if what_to_append > n:
                    res = 'NO'
                    break
    if not stack:
        while True:
            stack.append(what_to_append)
            #print('append',stack)
            op.append('+')
            if what_to_append == num:
                x = stack.pop()
                #print('pop',stack)
                op.append('-')
                wanted.append(x)
                what_to_append+=1
                break
            what_to_append +=1
            if what_to_append > n:
                res = 'NO'
                break
if res == 'NO':
    print(res)
else:
    for i in op:
        print(i)