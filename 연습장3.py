from collections import deque

N, M = map(int,input().split())

MAP = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:


# 조합.
# 스택을 이용한 조합 vs 재귀를 이용한 조합


# 스택을 이용해서 조합을 구하는 경우
# 마지막 인덱스를 이용했다. 

li = ['a','b','c','d','e']

deck = deque()
