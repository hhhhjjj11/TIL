# 알아두기 1. 뭐 해보고 비교한다음 둘중에 하나 선택해야할 때 임시변수에 담아서 실행해보는 식으로 할 수도 있다.
# 알아두기 2. 인덱스 조정법 : index = index%(len(li))이랑 
# 알아두기 3. 'X'표 없을때까지 움직이는로직. while li[i] == 'X'

import copy

N, M = map(int,input().split())

index = list(map(int,input().split()))
index = list(map(lambda x:x-1,index))

cnt = 0

li = [0]*N

idx_now = 0

res = 0 

for idx_goal in index:
    #print('idx_goal',idx_goal)
    # 현재에서 목표까지 한칸 씩 이동할건데 X 없을때만 세줄거임
    # 왼쪽으로가는거 한 번 세고 오른쪽으로 가는거 한 번 세고.

    temp1= copy.deepcopy(idx_now)
    temp2= copy.deepcopy(idx_now)     
    
    right = 0
    left = 0

    while temp1 != idx_goal :
        temp1 += 1
        temp1 %= N  
        if li[temp1] !='X':
            right += 1

    while temp2 != idx_goal :
        temp2 -= 1
        temp2 %= N
        if li[temp2] != 'X':
            left += 1   

    m = min(left,right)
    res += m

    idx_now = idx_goal
    li[idx_now] = 'X'

    idx_now += 1
    idx_now %= N

    if li[idx_now] == 'X':
        while li[idx_now] == 'X':   
            if li.count('X') ==N:
                break
            idx_now += 1
            idx_now %= N

print(res)        