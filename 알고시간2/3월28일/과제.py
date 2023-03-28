from itertools import combinations

T = int(input())

for tc in range(1,T+1):
    num, cnt = input().split()
    num = list(map(int,list(num)))
    cnt = int(cnt)
    num2 = sorted(num)
    M_idx = 0
    #print('num2',num2)
    TEMP1 = []
    X_before = 0
    while cnt>0:
        if num2:
            #print('num2',num2)
            X = num2.pop()
            #print("X,X_before",X,X_before)
            # print('temp1',TEMP1)
            if X != X_before:
                TEMP1 =[]
                #print(X,X_before,'temp reset')

            for _ in range(X):
                X_before += 1
            #print('X',X)
            for i in range(len(num)-1,-1,-1):
                if num[i]==X:
                    index = i
                    #print('가장큰수index',i)
                    break
            temp = 0
            for _ in range(num[M_idx]):
                temp += 1

            #print('현재가장큰자리에있는 애', temp)
            IDX = 0
            for _ in range(M_idx):
                IDX += 1
            #print('IDX',IDX)
            #print('index',index)
            # 만약에 최대값이랑 바꿀자리에 있는애가 같으면 넘어감.
            if IDX == index:
                M_idx +=1
                continue
            # 만약에 바꾸면 더작아지는데 겹치는애들이 있으면
            JB = False
            if num[IDX] > num[index]:
                for aa in num:
                    if num.count(aa) > 1:
                        JB = True
                        break
            if JB:
                cnt -=1
                continue
            num[IDX] = X
            num[index] = temp
            TEMP1.append(index)
            #print('TEMP1',TEMP1)
            if len(TEMP1)>1:
                #print('ddsdfsdf')
                #print(TEMP1)
                #print('num',num)
                LIST = list(combinations(TEMP1,2))
                for p in range(len(LIST)):
                    LIST[p] = sorted(LIST[p])
                #print('LIST',LIST)
                for idx1,idx2 in LIST:
                    # 뒤에있는게 더 숫자가 크면
                    if num[idx1] < num[idx2]:
                        #print('dddd')
                        V1 = 0
                        V2 = 0
                        #print('idx1',idx1,'idx2',idx2)
                        for _ in range(num[idx1]):
                            V1 += 1
                        for _ in range(num[idx2]):
                            V2 += 1
                        num[idx1] = V2
                        num[idx2] = V1
            #print('num',num)
            M_idx +=1
            cnt-=1
        else:
            JB = False
            for aa in num:
                if num.count(aa) > 1:
                    JB = True
                    break
            if JB:
                cnt -=1
                continue
            A,B = 0,0
            for _ in range(num[-1]):
                A+=1
            for _ in range(num[len(num)-2]):
                B+=1
            num[-1] = B
            num[len(num)-2] = A
            cnt-=1

    res=  0
    N = len(num)
    for idx, val in enumerate(num):
        res += val*(10**(N-1-idx))
    print(f'#{tc} {res}')