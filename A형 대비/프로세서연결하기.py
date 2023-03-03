T = int(input())

for tc in range(1,T+1):
    res = 0
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    stack = []

    while stack:
        board = stack.pop()
        # 보드에서 각각의 홈버튼에 대하여 인접항으로 뻗어나간다. visited에 체크하고, 만약 벽을 만나면 해당 홈버튼을 리스트에서 지운다.
        #
        for adj in range Adj:


    print(f'#{tc} {res}')