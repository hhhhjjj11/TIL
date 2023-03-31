T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())

    A = list(map(int,input().split()))

    cnt = 0

    index_list = list(range(N))

    # 인덱스 리스트를 가지고 조합을 찾는다.
    # 이때 조합의 수가 1,2,3, ... , N

    # 각 n에대해 조합의 개수가 n인 경우를 매번 새롭게 찾을 필요 없겠다.
    # 왜냐하면 어차피 N개의 조합을 만들어가는 과정에 N이하 개의 조합의 경우가 모두 거쳐가므로.

    stack = [[[x], A[x]] for x in index_list]

    while stack:
        combs, total = stack.pop()
        if total == K:
            cnt += 1

        # 조합을 다 구하면 더이상 원소를 추가하지 않는다.
        # 생각. 이거 빼도 될것 같은데.. 왜냐하면 원소개수가 다차면 어차피 더이상 append 할 것도 없어.
        # if len(combs) == N:
        #     continue

        # 조합수집하기
        else:
            for i in range(combs[-1]+1, N):
                if i not in combs:
                    # 가지치기
                    if total+A[i] > K:
                        continue
                    else:
                        stack.append([combs+[i], total+A[i]])


    print(f'#{tc} {cnt}')