for t in range(1,11):
    tc=int(input())
    input_li = []
    for i in range(100):
        input_li.append(list(map(int, input().split())))
    reslist = []
    for i in range(100):
        sum=0
        for j in range(100):
            sum+=input_li[i][j]
        reslist.append(sum)
    for i in range(100):
        sum=0
        for j in range(100):
            sum+=input_li[j][i]
        reslist.append(sum)
    diagSum1=0
    for i in range(100):
        diagSum1+=input_li[i][i]
    reslist.append(diagSum1)
    diagSum2=0
    for i in range(100):
        diagSum2+=input_li[i][99-i]
    reslist.append(diagSum1)
    d=max(reslist)
    print(f'#{t} {d}')