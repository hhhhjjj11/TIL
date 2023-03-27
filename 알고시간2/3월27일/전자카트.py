T = int(input())

def permf(i,k): # i: 값을 결정할 자리, k: 결정할 개수
    if i==k:
        # print(*p)
        perms.append([*p])
    else:
        for j in range(i, k): # 자신부터 오른쪽 원소들과 교환
            p[i],p[j] = p[j],p[i]
            permf(i+1,k)
            p[i],p[j] = p[j],p[i]

# p = [1,2,3]
# perm(0, 3)

for tc in range(1,T+1):
    perms = []
    N = int(input())
    li = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    p = list(range(2,N+1))
    min = 10000000
    permf(0, N-1)
    #print('perms',perms)
    for perm in perms:
        temp = 0
        temp+= li[0][perm[0]-1]
        #print('temp',temp)
        for i in range(len(perm)-1):
            temp+=li[perm[i]-1][perm[i+1]-1]
            #print('temp',temp)
            if temp>min:
                break
        if temp>min:
            continue
        temp += li[perm[-1]-1][0]
        if temp < min:
            min = temp

    print(f'#{tc} {min}')

