# 좋아보이는 풀이
import sys

def solution():
    n , *nums = map(int,sys.stdin.buffer.read().splitness())
    s = []
    answer = []
    cur = 1 # 커렌트 변수 사용해서 카운팅. 
    for value in nums:
        while cur <= value:
            answer.append('+')
            s.append(cur)
            cur += 1
            if s.pop() != value:
                return 'NO'
            # 어차피 꺼냈을때 다음항이 아니면 꺼낸거 그냥 버려야되는거임. 
            # 하나라도 그냥 버리면 원하는 수열 절대 못만듬★
            
        answer.append('-')

    return '\n'.join(answer)

print(solution())    


# 나의 풀이....
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