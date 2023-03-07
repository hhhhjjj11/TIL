T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    flag = [list(input()) for _ in range(N)]


    minV = 2500
    cnt = 0

    for i1 in range(N-2):
        cnt = 0
        if flag[i1][0] != 'W':
            flag[i1][0] = 'W'
            cnt += 1
        else:
            pass
        for i2 in range(i1+1, N-1):
            if flag[i2][0] != 'B':
                flag[i2][0] = 'B'
                cnt += 1
            else:
                pass
            for i3 in range(i2+1, N):
                if flag[i3][0] != 'R':
                    flag[i3][0] = 'R'
                    cnt += 1
                else:
                    pass

                for j in range(1, M):  # 세로 한줄 만들었으니 가로로 넓혀감
                    for i in range(N):
                        if i == i1:
                            if flag[i][j] != 'W':
                                flag[i][j] = 'W'
                                cnt += 1
                        elif i == i2:
                            if flag[i][j] != 'B':
                                flag[i][j] = 'B'
                                cnt += 1
                        elif i == i3:
                            if flag[i][j] != 'R':
                                flag[i][j] = 'R'
                                cnt += 1

        if minV > cnt:
            minV = cnt

    print(minV)