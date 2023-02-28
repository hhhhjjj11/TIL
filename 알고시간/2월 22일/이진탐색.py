T = int(input())

def level(X):
    n = 1
    while True:
        if 2**(n-1) <= X < 2**n:
            res = n
            break
        n+=1
    return res

def inorder(X):

    global NUM
    if X <= N and TREE[X] != '-':
        if X*2<=N:
            inorder(X*2)
        TREE[X]= NUM
        NUM+=1
        if X*2<=N:
            inorder(X*2+1)

for tc in range(1,T+1):
    global NUM
    NUM = 1
    res = 0
    N = int(input())
    LEVEL = level(N)
    TREE = ['-']*(2**(LEVEL))
    for i in range(N+1):
        TREE[i]=i
    inorder(1)

    print(f'#{tc} {TREE[1]} {TREE[N//2]}')