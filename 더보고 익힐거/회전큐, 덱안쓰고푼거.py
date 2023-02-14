import copy

N, M = map(int,input().split())

index = list(map(int,input().split()))
index = list(map(lambda x:x-1,index))

#print('index',index)
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
        #print('temp1',temp1)

        temp1 += 1
        temp1 %= N
        
        if li[temp1] !='X':
            right += 1

    while temp2 != idx_goal :
        #print('temp2',temp2)
        
        temp2 -= 1
        temp2 %= N
        
        if li[temp2] != 'X':
            left += 1   

    #print('left',left,'right',right)
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