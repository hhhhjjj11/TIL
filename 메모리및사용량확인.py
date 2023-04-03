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

from collections import deque

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    deck = deque([[N,0]])
    YS = list(range(4))
    res = 0
    resolved = False
    while deck:
        num, cnt = deck.popleft()
        for ys in YS:
            if ys == 0 and 1<=num+1<=1000000:
                if num+1 == M:
                    res = cnt+1
                    resolved =True
                    break
                else:
                    deck.append([num+1,cnt+1])
            elif ys == 1 and 1<=num-1<=1000000:
                if num-1 == M:
                    res = cnt+1
                    resolved = True
                else:
                    deck.append([num-1,cnt+1])
            elif ys == 2 and 1<=num*2<=1000000:
                if num*2 == M:
                    res = cnt +1
                    resolved = True
                else:
                    deck.append([num*2,cnt+1])
            elif ys ==3 and 1<=num-10 <=1000000:
                if num-10 ==M:
                    res = cnt+1
                    resolved= True
                else:
                    deck.append([num-10, cnt + 1])
        if resolved:
            break
    print(f'#{tc} {res}')

# 코드 끝
# 실행 시간: 206.12s
# 메모리 사용량: 약 31200 KB + 110KB

cur_mem, peak_mem = tracemalloc.get_traced_memory()

print(f'Execution: {time.time() - st : .3f}s')
print(f'Memory: {peak_mem/1024. : .3f}KB')
tracemalloc.stop()