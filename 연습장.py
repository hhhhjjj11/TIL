T = int(input())

for tc in range(1,T+1):
    
    s = input()

    stack= [s[0]]
    idx = 1
    while True:
        if idx >= len(s)-1:
            break
        if len(stack)==0 or stack[-1] != s[idx]:
            stack.append(s[idx])
            idx += 1
        else:
            dlted = stack.pop()
            while True:
                idx += 1
                if idx >= len(s)-1 and dlted != s[idx]:
                    break


    print(stack)
    print(f'#{tc} {len(stack)}')