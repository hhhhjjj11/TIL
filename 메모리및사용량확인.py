import tracemalloc
import time
import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline

tracemalloc.start()
st = time.time()
mod = 1000000007
# 코드 시작
import sys
sys.setrecursionlimit(10**6)

N = int(input())

# DP ={}

# # 1열까지 
# DP[1] = 3
# # 2열
# DP[2] = 7
# # 3열
# DP[3] = 17

def f(X):
    if X >3 :
        return f(X-2)*5 + f(X-3)*2
    if X ==1:
        return 3
    if X ==2:
        return 7
    if X ==3 :
        return 16

# for n in range(4,N+1):
#     DP[n] = DP[n-2]*5 + DP[n-3]*2

print(f(N)%9901)
# 코드 끝
# 실행 시간: 206.12s
# 메모리 사용량: 약 31200 KB + 110KB

cur_mem, peak_mem = tracemalloc.get_traced_memory()

print(f'Execution: {time.time() - st : .3f}s')
print(f'Memory: {peak_mem/1024. : .3f}KB')
tracemalloc.stop()