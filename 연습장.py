T = int(input())

for tc in range(1,T+1):
    res = 0
    N = int(input())
    li = (list(map(int,input().split())) for i in range(N))

    visited = [False]*N

    for j in range(N):
        
        sum = li[0][j]
        stack = [(0,j)]

        i = 0

        visited[j] = True
        
        while stack:
            
            I,J = stack.pop()
            
            i += 1
            for j2 in range(N):
                if not visited[j2]:
                    stack.append((i,j2))
                    visited[j2] = True
                    break
 
    print(f'#{tc} {res}')