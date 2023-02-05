from pprint import pprint


T = int(input())

for tc in range(T):
    N,M,K=map(int,input().split())

    li=[]
    for i in range(M):
        tem=[0]*N
        li.append(tem)

    for _ in range(K):
        i,j=map(int,input().split())
        li[j][i] = 1

    
    cnt = 0
    for i in range(M):
        for j in range(N):
            if li[i][j]==0:
                #print(f'{i,j}통과')
                continue
            elif li[i][j]==1:
                #print(f'{i,j}배추')
                if i==0 and j==0:
                    ard=[li[0][1], li[1][0]]
                elif i==0 and j==N-1:
                    ard=[li[0][N-2], li[1][N-1]]
                elif i==M-1 and j==0:
                    ard=[li[M-2][0], li[M-1][1]]
                elif i==M-1 and j==N-1:
                    ard=[li[M-1][N-2], li[M-2][N-1]]
                elif i==0:
                    ard=[li[i+1][j], li[i][j+1], li[i][j-1]]
                elif i==M-1:
                    ard=[li[i][j+1], li[i][j-1], li[i-1][j]]
                elif j==0:
                    ard=[li[i+1][j], li[i][j+1], li[i-1][j]]
                elif j==N-1:
                    ard=[li[i+1][j], li[i][j-1], li[i-1][j]]
                else:
                    ard=[li[i+1][j], li[i][j-1], li[i-1][j], li[i][j+1]]

                if ard.count('C') == 0 : 
                    #print(f'{i,j}배추, 주변에C 없음, +1')
                    cnt +=1
                    li[i][j] = 'C'
                elif ard.count('C') > 0 :
                    # c=ard.count('C')
                    #print(f'{i,j}배추, 주변에C {c}개 있음, +0')
                    #pprint(li)
                    li[i][j] = 'C'

    #pprint(li)
    print(cnt)

