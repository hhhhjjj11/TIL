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



# 코드 끝
# 실행 시간: 206.12s
# 메모리 사용량: 약 31200 KB + 110KB

cur_mem, peak_mem = tracemalloc.get_traced_memory()

print(f'Execution: {time.time() - st : .3f}s')
print(f'Memory: {peak_mem/1024. : .3f}KB')
tracemalloc.stop()