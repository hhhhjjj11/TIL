T = int(input())

for _ in range(T):
    N = int(input())

    li = [0]*(N+1)

    # li[서류성적] = 면접성적
    # 어떤놈이 서류성적도 뒤에있는데 
    # 면접성적도 뒤에있으면 
    # 떨군다
    # 앞에서부터
    # 자기 앞에있는 놈들에 대해 
    # 앞에있는놈들중에서 최고순위 보다 커야됨
    # 안그러면 탈락

    for _ in range(N):
        a, b = map(int,input().split())
        li[a] = b
    #print('li',li)
    cnt = 0
    highest_grade = N+1  # 서류1등이 면접꼴찌 li[1]=N 일 수도 있으니까. 처음에는 최고등수를 N으로하면 안됨.
    for i in range(1,N+1): 
        # 내앞의 최고 순위보다 내가 무조건 커야 산다.

        if li[i] < highest_grade:
            
            highest_grade = li[i]
            cnt+=1
        # 그렇지 않으면 앞에 나보다 둘다 잘본애가있단얘기니까 걸러

    print(cnt)