def inorder(X):

    global res
    if X <= N and TREE[X] != 0:
        if X*2<=N:
            inorder(X*2)
        res += TREE[X]
        if X*2<=N:
            inorder(X*2+1)


for tc in range(1,11):
    N = int(input())
    TREE = [0]*(N+1)
    for i in range(N):
        li = input().split()
        node, V = int(li[0]), li[1]
        TREE[node] = V
    res = ''
    inorder(1)

    print(f'#{tc} {res}')