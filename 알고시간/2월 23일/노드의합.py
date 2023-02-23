T = int(input())

for tc in range(1,T+1):
    res = 0
    N, M, L = map(int,input().split())
    # N : 노드개수 , M : 리프노드개수 , L : 원하는 노드 번호

    TREE = [0]*(N+1)

    for _ in range(M):
        node_num , value = map(int,input().split())
        TREE[node_num] = value

    for i in range(N,0,-1): #N부터 1씩 감소
        if i % 2 == 0 : #첫번째자식에 대하여
            if i+1<=N: #두번째자식이 있음
                childSum = TREE[i] + TREE[i+1]
                TREE[i//2] = childSum
            else: #두번째자식 없음, (마지막노드)
                TREE[i//2] = TREE[i]

    print(f'#{tc} {TREE[L]}')