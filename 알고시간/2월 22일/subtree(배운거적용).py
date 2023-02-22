T = int(input())

def preorder(X):
    global cnt
    cnt += 1
    while X in graph : # 자식이 있다는 얘기
        preorder(graph.index(X))
        graph[graph.index(X)] = 0

for tc in range(1,T+1):

    E, N = map(int,input().split())
    li = list(map(int,input().split()))
    graph = [0]*(E+2)

    # 자식번호를 인덱스로
    for i in range(E):
        parent, child = li[i*2],li[i*2+1]
        graph[child] = parent

    global cnt
    cnt = 0

    preorder(N)

    print(f'#{tc} {cnt}')

