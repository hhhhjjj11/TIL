T = int(input())

for tc in range(1,T+1):
    s = input()
    stk1 =[]
    stk2 =[]
    for i in range(len(s)):
        if s[i] == '(':
            stk1.append(1)
        elif s[i] == ')':
            if len(stk1)==0:
                print(f'#{tc} 0')
                continue
            stk1.pop()
        elif s[i] == '{':
            stk2.append(1)
        elif s[i] == '}':
            if len(stk1)==0:
                print(f'#{tc} 0')
                continue
            stk2.pop()
 
    res = 0
    
    if len(stk2) == 0 and len(stk1) == 0:
        res = 1

    print(f'#{tc} {res}')