for tc in range(1,11):
    res= 0
    beak = int(input())
    table = [list(map(int,input().split())) for _ in range(100)]

    for j in range(100):
        temp = []
        for i in range(100):
            if table[i][j] != 0:
                temp.append(table[i][j])
                table[i][j] = 0
        for i in range(len(temp)-1):
            if temp[i] == 1 and temp[i+1] == 2:
                res += 1

    print(f'#{tc} {res}')