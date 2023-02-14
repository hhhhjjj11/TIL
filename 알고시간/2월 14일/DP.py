T = int(input())

Memo = [0]*31

def myfunc(N):
    
    if N == 1:
        Memo[N] = 1
        return Memo[N]
    elif N == 2:
        Memo[N] = 3
        return Memo[N]
    else:
        if Memo[N]:
            return Memo[N]
        else:    
            Memo[N] = myfunc(N-1) + 2*myfunc(N-2)
            return Memo[N]


for tc in range(1,T+1):
    X = int(input())
    X//=10
    print(f'#{tc} {myfunc(X)}')