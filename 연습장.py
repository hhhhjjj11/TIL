T = int(input())

for tc in range(1,T+1):

    N = int(input())
    li = [list(map(int,input().split())) for _ in range(N)]

    p = list(range(N)) # 0 ~ N-1

    stack = [[value]  for value in p]
    stack2 = [(li[0][value]/100) for value in p]
    perms = []

    M = 0

    while stack:
        per = stack.pop() # 순열, 사용한인덱스
        temp = stack2.pop()
        #print('꺼냄',per,temp)
        if len(per) == len(p):
            if temp > M:
                #print('M=temp')
                M = temp
                #print('M',M)
        else:
            for i in range(N):
                if not i in per:
                    # 0부터 N-1까지 중에 per에 없으면
                    # 0 2 1
                    #print('i','temp',i,temp)
                    if M > temp * ((li[len(per)][i])/100):
                        continue
                    else:
                        stack.append(per + [i])
                        stack2.append(temp * ((li[len(per)][i])/100))
                        break

    print(f'#{tc}',end=' ')
    print("{:.6f}".format(M*100))