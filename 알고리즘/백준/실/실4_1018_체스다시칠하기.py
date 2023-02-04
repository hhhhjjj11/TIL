N, M = map(int,input().split())

chess =[]

for _ in range(N):
    chess.append(list(input()))


results = []

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for p in range(8):
            for q in range(8):
                if (p+q) % 2 == 0 and chess[i+p][j+q] !='B':
                    cnt += 1
                elif (p+q) % 2 == 1 and chess[i+p][j+q] !='W':
                    cnt += 1
        results.append(cnt)
        cnt = 0
        for p in range(8):
            for q in range(8):
                if (p+q) % 2 == 0 and chess[i+p][j+q] !='W':
                    cnt += 1
                elif (p+q) % 2 == 1 and chess[i+p][j+q] !='B':
                    cnt += 1
        results.append(cnt)

print(min(results))




