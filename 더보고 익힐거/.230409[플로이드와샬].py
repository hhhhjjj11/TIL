# 11403 경로찾기 백준

N = int(input())

adj_matrix = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adj_matrix[i][k] == 1 and adj_matrix[k][j] == 1:
                adj_matrix[i][j] = 1

for row in adj_matrix:
    print(' '.join(map(str,row)))