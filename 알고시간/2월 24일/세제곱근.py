T = int(input())

for tc in range(1,T+1):
    N = int(input())

    temp = 1
    res = -1
    while temp**3 <= N:
        if temp**3 == N:
            res = temp
            break
        temp+=1

    print(f'#{tc} {res}')