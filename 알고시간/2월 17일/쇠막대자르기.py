T = int(input())

for tc in range(1,T+1):
    res = 0
    state = input()
    sticks = 0    # 걸려있는 쇠막대의 수
    for i in range(len(state)):
        if state[i] == '(' and state[i+1] == ')':  # 레이저
            res += sticks
            #print('res',res)
        elif state[i] == '(' and state[i+1] != ')':
            sticks += 1
        elif state[i] == ')' and state[i-1] != '(':
            res += 1
            sticks -= 1
        elif state[i] == ')' and state[i-1] == '(':
            pass

    print(f'#{tc} {res}')