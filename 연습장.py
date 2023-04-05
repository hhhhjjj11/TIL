from collections import deque
inf = float('inf')
def solve():
    n = int(input())
    # 확률..
    prob = [list(map(int, input().split())) for _ in range(n)]
    # 2^n개 -1생성
    
    dp = [-1 for _ in range(1 << n)]
    # 첫항은 1로
    dp[0] = 1
    que = deque([0])
    for i in range(n):
        for _ in range(len(que)):
            # 덱에서 꺼낸거를 상태
            status = que.popleft()
            for j in range(n): # J : 0~ n-1
                # 상태랑 비트마스킹이 겹치는게없으면
                if not status & (1 << j):
                    # dp는 -1
                    if dp[status | (1 << j)] == -1:
                        que.append(status | (1 << j))
                    dp[status | (1 << j)] = max(dp[status] * prob[i][j], dp[status | (1 << j)])
    p = dp[-1] * 100 / (10**(n << 1))
    p = round(p, 6)
    p = str(p)
    a, b = p.split('.')
    b += '000000'
    return f'{a}.{b[:6]}'
for tc in range(1, int(input()) + 1):
    print(f'#{tc} {solve()}')