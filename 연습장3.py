T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, n, string):
    if n == 7:
        setset.add(string)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, n+1, string+table[nx][ny])



for tc in range(1, T+1):
    table = [list(map(str, input().split())) for _ in range(4)]
    setset = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, table[i][j])

    print(f'#{tc}', len(setset))