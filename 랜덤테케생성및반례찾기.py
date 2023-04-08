from random import randint
# subprocess.call

# 예제 생성
def example():
    N  =randint(2,5)
    nums = []
    for _ in range(N):
        nums.append(randint(1,100))
    op = []
    total = 0
    for _ in range(N):
        total +=1
    
    for k in range(4):
        if k ==3:
            op.append(total-1)
            continue
        X = randint(0, total-1)
        op.append(X)
        total -= X
    return N,nums,op    

# 맞은 답

from collections import deque
max_result = 0
min_result = 0

def right_sol(n,number,op):
    global max_result, min_result
    add, sub, mul, div = op
    max_result = - int(1e9)
    min_result = int(1e9)

    def dfs(add, sub, mul, div, sum, idx):
        global max_result, min_result
        if idx == n:
            max_result = max(max_result, sum)
            min_result = min(min_result, sum)
            return
        if add:
            dfs(add-1, sub, mul, div, sum + number[idx], idx + 1)
        if sub:
            dfs(add, sub-1, mul, div, sum - number[idx], idx + 1)
        if mul:
            dfs(add, sub, mul-1, div, sum * number[idx], idx + 1)
        if div:
            dfs(add, sub, mul, div-1, int(sum / number[idx]), idx + 1)
            
    dfs(add, sub, mul, div, number[0], 1)
    return max_result, min_result


# 틀린 답
from collections import deque

def wrong_sol(N, nums, op):


    M = 0
    m = 10 ** 9

    deck = deque()
    deck.append([1, nums[0], op[:]]) 

    while deck:
        cnt ,res, op2 = deck.popleft()
        # print('cnt',cnt)
        # print('res',res)
        # print('op2',op2)
        if cnt == N and sum(op2) == 0: # 계싼이 끝났고 연산자가 남아있지 않으면
            if res < m:
                m = res
            if res > M:
                M = res
            continue
        
        for i in range(4):
            if op2[i] != 0: # 남아있는게 있으면
                op2[i] -=1
                if i == 0:
                    deck.append((cnt+1,res+nums[cnt],op2[:]))
                elif i == 1:
                    deck.append((cnt+1, res-nums[cnt],op2[:]))
                elif i == 2:
                    deck.append((cnt+1, res*nums[cnt],op2[:]))
                elif i == 3:
                    if res < 0:
                        deck.append((cnt+1, -((-res)//nums[cnt]),op2[:]))
                    else:    
                        deck.append((cnt+1, res//nums[cnt],op2[:]))
                op2[i]+=1

    return M, m




# 반례 출력
def check():
	ex = example()
	right = right_sol(ex[0], ex[1],ex[2])
	wrong = wrong_sol(ex[0], ex[1],ex[2])
	if right != wrong:
		print(ex[0], ex[1],ex[2])

		print("맞은 답:", right)
		print("틀린 답:", wrong)
		return
	else:
		check()

check()