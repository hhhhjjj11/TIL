from pprint import pprint

T = int(input())

for tc in range(1,T+1):
    res = 0

    N, M = map(int,input().split())

    li = [[0]*N for _ in range(N)]

    # 게임시작할때
    n = N//2
    li[n][n] = 'W'
    li[n-1][n-1] = 'W'
    li[n][n-1] = 'B'
    li[n-1][n] = 'B'

    #pprint(li)

    adj = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,1),(-1,-1)]

    for i in range(M):
        x, y, clr = list(map(int,input().split()))
        i, j = y-1, x-1
        #print('i,j,clr' ,i,j,clr)
        if clr == 1:      # 흑돌
            li[i][j] = 'B'
            for idx in adj:
                temp = []
                plus = 1
                while True:
                    I_adj, J_adj = i+idx[0]*plus, j+idx[1]*plus
                    #print('Iadj,Jadj',I_adj,J_adj)
                    if 0<= I_adj <N and 0<=J_adj<N :
                        ADJ = li[I_adj][J_adj]
                        if ADJ == 0:
                            break
                        elif ADJ == 'W':
                            temp.append((I_adj,J_adj))
                            plus += 1
                        elif ADJ == 'B':
                            #print('temp',temp)
                            if not temp:
                                break
                            else:
                                for temp_idx in temp:
                                    li[temp_idx[0]][temp_idx[1]] = 'B'
                                # for X in li:
                                #     print(X)
                                break
                    else:
                        break

        elif clr == 2: # 백돌
            li[i][j] = 'W'
            for idx in adj:
                temp = []
                plus = 1
                while True:
                    I_adj, J_adj = i+idx[0]*plus, j+idx[1]*plus
                    if 0<= I_adj <N and 0<=J_adj<N :
                        ADJ = li[I_adj][J_adj]
                        if ADJ == 0:
                            break
                        elif ADJ == 'B':
                            temp.append((I_adj,J_adj))
                            plus += 1
                        elif ADJ == 'W':
                            if not temp:
                                break
                            else:
                                for temp_idx in temp:
                                    li[temp_idx[0]][temp_idx[1]] = 'W'
                            # for X in li:
                            #     print(X)
                            break
                    else:
                        break

    #pprint(li)
    num_of_B = 0
    num_of_W = 0
    for i in range(N):
        for j in range(N):
            if li[i][j] == 'B':
                num_of_B += 1
            elif li[i][j] == 'W':
                num_of_W += 1

    print(f'#{tc} {num_of_B} {num_of_W}')