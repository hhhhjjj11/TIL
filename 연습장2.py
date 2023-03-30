T = int(input())

for tc in range(1,T+1):
    res = 0
    N, M = map(int,input().split())

    li1 = list(map(int, input().split()))
    li1.sort()
    li2 = list(map(int, input().split()))
    cnt = 0
    for b in li2:
        #print(f'{b} 시작')
        left = 0
        right = N-1
        toggle = 'ready'
        results =[]
        while left <= right:
            middle = (left+right)//2
            if b == li1[middle]:
                results.append(('b','index',b,middle))
                #print(f'일치,{middle}')
                cnt += 1
                break
            elif b > li1[middle]:
                left = middle + 1
                if toggle == 'left side' or toggle == 'ready':
                    toggle = 'right side'
                    #print(f'오른쪽에위치,{middle}')
                else:
                    #print('오오.여기걸림1',{middle})
                    break
            else:
                right = middle - 1
                if toggle == 'right side' or toggle == 'ready':
                    toggle = 'left side'
                    #print(f'왼쪽에위치,{middle}')
                else:
                    #('왼왼.여기걸림2',{middle})
                    break
        #print('b:',b,'results',results)


    print(f'#{tc} {cnt}')