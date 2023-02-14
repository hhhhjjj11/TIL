T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    M = max(arr)
    results = []
    for i in range(N):
        li=['O']*M
        for j in range(arr[i]):
            li[j]='B'
        results.append(li)

    #print(results)
    answers=[]
    for j in range(M):  # 각 열에 대해
        ans=0
        meet = False
        for i in range(N):   # 각행을 따지는데
            if results[i][j]=='B':
                meet = True    
                for k in range(i):
                    results[k][j]='N'
            if meet:
                break

        for i in range(N):
            if results[i][j]=='O':
                ans+=1
        answers.append(ans)


    #print(results)
    M2=0
    for item in answers:
        if item>=M2:
            M2=item
    
    print(f'#{tc} {M2}')

    # 좌표 평면마냥 쫙 깔아놓고 세는식으로 풀면 쉽다는 점 기억하자