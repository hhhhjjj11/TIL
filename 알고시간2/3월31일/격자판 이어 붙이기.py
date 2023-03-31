T = int(input())

for tc in range(1,T+1):
    res = 0
    li = [list(input().split()) for _ in range(4)]

    Adj = [(0,1),(1,0),(0,-1),(-1,0)]

    # 각각의 자리에서,,,, 원래자리 + 6번이동해서 추가한 문자열 을 set에저장한다.
    # 그런데 이렇게 하면 무한루프 돌것같은데..?
    # 네방향 dfs로 해야할듯..

    results = set()

    for i in range(4):
        for j in range(4):
            # 각각의 시작점에서 dfs
            stack = [(i,j,li[i][j])]
            while stack:
                ni, nj, value = stack.pop()

                if len(value) == 7:
                    results.add(value)
                    continue
                for adj in Adj:
                    nexti, nextj = ni + adj[0], nj + adj[1]
                    # 칸을 벗어나지 않으면
                    if 0<= nexti < 4 and 0<= nextj < 4:
                        stack.append((nexti,nextj,value+li[nexti][nextj]))


    print(f'#{tc} {len(list(results))}')