T = int(input())

for tc in range(1,T+1):
    res = 0
    N = int(input())

    li = [list(map(int,input().split())) for i in range(N)]

    stack = [([value],[idx]) for idx,value in enumerate(li[0])]

    row = 0

    m = 100

    while stack:
        #print('stack',stack)
        S, index = stack.pop()
        
        #print('S',S)
        if len(S) == N:
            if sum(S)<=m:
                m = sum(S)
            continue
        
        row = len(S)
        
        for j in range(N):
            #print('row',row,'j',j)
            if j in index or (sum(S)+li[row][j]) >= m :
                continue
            else:
                stack.append((S+[li[row][j]], index+[j]))
            
    print(f'#{tc} {m}')