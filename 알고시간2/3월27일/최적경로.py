T = int(input())

def perm(i,k): # i: 값을 결정할 자리, k: 결정할 개수
    if i==k:
        print(*p)
        perms.append([*p])
    else:
        for j in range(i, k): # 자신부터 오른쪽 원소들과 교환
            p[i],p[j] = p[j],p[i]
            perm(i+1,k)
            p[i],p[j] = p[j],p[i]


for tc in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    Cx = li.pop(0)
    Cy = li.pop(0)
    Hx = li.pop(0)
    Hy = li.pop(0)

    perms = []
    p = list(range(N))

    perm(0,N)
    print('perms',perms)