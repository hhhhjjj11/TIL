T = int(input())

for tc in range(1,T+1):

    li=[]
    for _ in range(10):
        li.append([0]*10)

    #print('li',li)

    ans=0

    N = int(input())

    for i in range(N):
        c = list(map(int,input().split()))
        x1,y1 = c[0],c[1]
        x2,y2 = c[2],c[3]

        if c[-1] == 1:
            for j in range(x1, x2+1):
                for k in range(y1, y2+1):
                    if li[j][k] == 'B':
                        ans +=1
                        li[j][k] = 'P'
                    elif li[j][k] == 0:
                        li[j][k] = 'R'
        elif c[-1] == 2:
            for j in range(x1,x2+1):
                for k in range(y1, y2+1):
                    if li[j][k]=='R':
                        ans+=1
                        li[j][k] = 'P'
                    elif li[j][k] == 0:
                        li[j][k] ='B'

    print(f'#{tc} {ans}')