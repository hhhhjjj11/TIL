N, L = map(int,input().split())

def f(N,L):
    temp = 0
    for i in range(L):
        temp += i
    if N - temp < L:
        res = -1
        return (0,res)
    elif (N-temp) % L == 0:
        mini = (N-temp)//L
        res = []
        for x in range(mini, mini+L):
            res.append(x)
        return (1,mini,res)
    return(0,0)

if f(N,L-1)[0] == 1 and f(N,L-1)[1] == 1:
    print(0,end=' ')
    for x in f(N,L-1)[2]:
        print(x,end= ' ')

else:
    while True:
        if L > 100:
            print(-1)
            break
        temp = 0
        for i in range(L):
            temp += i
        if N - temp < L:
            print(-1)
            break
        elif (N-temp) % L == 0:
            mini = (N-temp)//L
            for x in range(mini, mini+L):
                print(x,end= ' ')
            break
        L += 1