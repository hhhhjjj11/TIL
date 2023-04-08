# 알아두기 : 
# 덱에서 리스트를 꺼내서 -> 리스트의 항을 append하는 것이아니라
# 항을 조작해서 다시 넣는다 -> 참조변수이기 때문에 오류가남
# 그러면 딥카피를 써야함
# 그래서 리스트를 덱에 넣는 것이 아니라! 덱의 각 항을 분할해서 덱에 넣는 식으로 한다.

# 아래 답안을 보면
# 나의 답안은 op리스트를 한번에 덱에 넣었다.
# 연산자를 쓸때마다 항을 1씩 줄여서 덱에 다시 넣고싶은데, 그러기위해 딥카피를 썼다.

# 반면 좋아보이는 답안에서는 op의 각 연산의 개수를 꺼낸다음 직접 덱에 넣는 식으로 했다.
# 이 경우 리스트 전체가 들어가는 것이 아니라서 얕은복사에 의한 오류가 발생하지 않는다.




# 좋아보이는 정답 -> 딥카피 안씀, 리스트 의 항들을 꺼내서 덱에직접넣음
n = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
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
print(max_result)
print(min_result)





from collections import deque

# 내정답 : 리스트를 통채로 덱에 넣음 -> 항조작 불가 -> 딥카피를 썼다.
N = int(input())

nums = list(map(int,input().split()))

op = list(map(int,input().split())) # +, -, *, //

M = - (10 ** 9)
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

print(M)
print(m)
            

