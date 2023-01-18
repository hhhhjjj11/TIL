T = int(input())
for t in range(1,T+1):
    sdoku=[0]*9
    for i in range(9):
        sdoku[i]=list(map(int,input().split()))
    #9x9 배열 완성
    row=1
    col=1
    box=1
    check=[0]*9
    for i in range(9):
        for j in range(9):
            check[sdoku[i][j]-1]+=1
        # print('check',check) # 1
        for j in range(9):
            if check[j]!=1:
                row=0
                break
        for j in range(9):
            check[j]=0
        # print('check',check) # 0
        for j in range(9):
            check[sdoku[j][i]-1]+=1
        # print('check',check) # 1
        for j in range(9):
            if check[j]!=1:
                col=0
                break
        for j in range(9):
            check[j]=0
        # print('check',check) # 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    check[sdoku[3*i+k][3*j+l]-1]+=1
            # print('check',check) # 1
            for k in range(9):
                if check[k]!=1:
                    box=0
                    break
            for k in range(9):
                check[k]=0
    if row==1&col==1&box==1:
        print(f'#{t} 1')
    else :
        print(f'#{t} 0')