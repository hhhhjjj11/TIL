for tc in range(1,11):
    n = int(input())
    res = []
    li =[]
    for i in range(100):
        li.append(list(map(int,input().split())))

    bottom = []
    # 도착점 배열
    for j in range(100):
        if li[99][j] == 1:
            bottom.append(j)

    #print(bottom)
    for i in range(len(bottom)):
        x, y = 99, bottom[i]
        cnt = 0
        # now = x,y
        dir = '위'
        while True:
            if x<=0:
                res.append((y,cnt))
                #print(res)
                break
            if dir =='위':
                if  0<y+1<100 and li[x][y+1] ==1:
                    y = y+1
                    cnt += 1
                    dir = '우'
                elif 0<y-1<100 and li[x][y-1] == 1:
                    y = y -1
                    cnt += 1
                    dir = '좌'
                else:
                    x = x-1
                    cnt += 1
            elif dir == '우':
                pass
                if li[x-1][y] == 1:
                    x = x-1
                    cnt += 1
                    dir = '위'
                else:
                    y = y+1
                    cnt += 1
            elif dir == '좌':
                pass
                if li[x-1][y]==1:
                    x=x-1
                    cnt += 1
                    dir='위'
                else:
                    y=y-1
                    cnt += 1

    res = sorted(res, key = lambda x : (x[1]))
    #print(res)
    M = res[0][0]

    print(f'#{tc} {M}')