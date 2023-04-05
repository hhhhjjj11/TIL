N = int(input())

li = [list(map(int,input().split())) for _ in range(N)]

memo = [[0]*3 for _ in range(N)]
memo[0] = li[0]

for i in range(1,N):
    memo[i][0] = min(memo[i-1][1],memo[i-1][2]) + li[i][0]
    memo[i][1] = min(memo[i-1][0],memo[i-1][2]) + li[i][1]
    memo[i][2] = min(memo[i-1][0],memo[i-1][1]) + li[i][2]

print(min(memo[N-1]))





# 틀린코드(메모리초과) (답은맞는듯)

from collections import deque

N = int(input())

li = [list(map(int,input().split())) for _ in range(N)]

deck = deque([['R',1, li[0][0]],['G',1, li[0][1]],['B',1,li[0][2]]])

# 마지막 색상(동시에 커서), 고려한갯수, 가중치

# 생각. visited를 한번에 쓰는 방법.
# 다익스트라가능? 안될것같은데
# 다익스트라라는 것은 각지점에서의 최대또는 최소값을 저장해두었다가 
# 탐색과정에서 그것이 갱신되는 경우에만 탐색을 이어나가는 것인데
# 될것같은데..?
# 두단계전까지는 무조건 최소가 최소 맞는것같은데?
# 두단계전의 색에 관계 없이, 아 그것도 아닌듯. 
# 두단계전까지 10인데 전단계에서 억 억 1 이렇게 비용들면
# 다익스트라의 사용조건 : 현재지점까지의 최대,최소가 그다음 지점을 계산할때 영향을 주냐 안주냐 차이인듯. 
# "n번지점까지의 최소가 A라 하더라도, 그 다음 지점을 따질때 따지지 못하는 값이 생기기 때문에 n번째지점까지의 최소경로가 전체 최소경로의 일부라고 장담할 수 없다." 

for input in li:
    R,G,B = input

m = 100000000
while deck:
    last_color, completed, V = deck.popleft()
    if completed == N:
        if V < m:
            m = V
        continue
    for idx, color in enumerate(['R','G','B']):
        if last_color == color:
            continue
        if V + li[completed][idx] >= m:
            continue
        deck.append([color,completed+1,V+li[completed][idx]])

print(m)



# 임시저장.. bfs
