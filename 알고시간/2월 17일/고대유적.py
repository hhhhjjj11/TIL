T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    li = [list(map(int,input().split())) for i in range(N)]

    adj = [(1,0,'down'),(0,1,'right')]

    cnts = []

    for i in range(N):
        for j in range(M):
            if li[i][j] == 0:
                continue
            elif li[i][j] == 1:
                for idx in adj:
                    if 0 <= i+idx[0] < N and 0 <= j+idx[1] < M and li[i+idx[0]][j+idx[1]] == 1:
                        plus = 1
                        cnt = 1
                        if idx[2] == 'down':
                            while 0< i+plus<N and li[i+plus][j] == 1:
                                plus += 1
                                cnt += 1
                            cnts.append(cnt)
                        elif idx[2] == 'right':
                            while 0< j+plus<M and li[i][j+plus] == 1:
                                plus += 1
                                cnt += 1
                            cnts.append(cnt)

    print(f'#{tc} {max(cnts)}')