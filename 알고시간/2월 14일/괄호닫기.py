T = int(input())

for tc in range(1,T+1):
    s = input()

    stack = []
    res = 1 
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack:
                res = 0
            elif stack[-1] == '(':
                stack.pop()
            elif stack[-1] != '(':
                res = 0
        elif s[i] == '}':
            if not stack:
                res = 0
            elif stack[-1] == '{':
                stack.pop()
            elif stack[-1] != '{':
                res = 0
    
    #print('stack',stack)
    if len(stack) != 0:
        res = 0

    
    print(f'#{tc} {res}')
