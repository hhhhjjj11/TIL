T = int(input())
for t in range(1,T+1):
    N=int(input())
    sdoku=[]
    for i in range(N):
        sdoku.append(list(map(int,input().split())))
    # 이차원배열 받았고.
    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(sdoku[N-1-j][i], end='')
        print(' ',end='')
        for j in range(N):
            print(sdoku[N-1-i][N-1-j], end='')
        print(' ',end='')
        for j in range(N):
            print(sdoku[j][N-1-i], end='')
        print()