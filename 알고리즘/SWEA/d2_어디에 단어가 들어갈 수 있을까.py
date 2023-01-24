T = int(input())

for t in range(1,T+1):
    cnt=0
    N, K = map(int,input().split())
    li=[]
    
    for _ in range(N):
        li.append(list(map(int,input().split())))
    
    # 가로확인
    #print('가로확인시작')
    for i in range(N):
        
        #print(f'{i}번째 행 검사 시작, cnt :',cnt)
        for j in range(N-K+1):
            if j == 0:
                #print(f'{i}행 첫열 검사시작')
                check=True
                for k in range(K):
                    if li[i][j+k]==1 and li[i][j+K]==0:
                        pass
                    else:
                        check=False
                if check==True:
                    cnt+=1
                    #print('첫열에서 발생',cnt)
            if 0 < j < N-K:
                #print(f'{i}행{j}열 검사시작')
                check=True
                for k in range(K):
                    if li[i][j-1]==0 and li[i][j+k]==1 and li[i][j+K]==0:
                        pass
                    else:
                        check=False
                if check==True:
                    cnt+=1
                    #print('중간에서발생',cnt)
            if j == N-K:
                #print(f'{i}행 마지막열 검사시작')
                check=True
                for k in range(K):
                    if li[i][j-1]==0 and li[i][j+k]==1 :
                        pass
                    else:
                        check=False
                if check==True:
                    cnt+=1
                    #print('마지막열에서발생',cnt)
         

    #세로확인
    #print('세로확인시작')
    for j in range(N):
        for i in range(N-K+1):
            if i == 0:
                #print(f'{j}열 첫행 검사시작')
                check=True
                for k in range(K):
                    if li[i+k][j]==1 and li[i+K][j]==0:
                        pass
                    else:
                        check=False
                if check==True:
                    cnt+=1
                    #print('첫행에서 발생',cnt)
            if 0 < i < N-K:
                #print(f'{j}열{i}행 검사시작')
                check=True
                for k in range(K):
                    if li[i-1][j]==0 and li[i+k][j]==1 and li[i+K][j]==0:
                        pass
                    else:
                        check=False
                if check==True:
                    cnt+=1
                    #print('중간에서발생',cnt)
            if i == N-K:
                #print(f'{j}열 마지막행 검사시작')
                check=True
                for k in range(K):
                    if li[i-1][j]==0 and li[i+k][j]==1 :
                        pass
                    else:
                        check=False
                if check==True:
                    cnt+=1
                    #print('마지막행에서발생',cnt)

               
    print(f'#{t} {cnt}')

