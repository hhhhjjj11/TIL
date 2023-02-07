arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

n = len(arr)

sub = []

for i in range(1 << n):
    s = set()
    for j in range(n):
        if i & (1 << j):
            s.add(arr[j])
    if len(s) != 0:
        sub.append(s)

T = int(input())

for tc in range(1, T + 1):

    N, K = map(int, input().split())

    res = 0

    for subset in sub:
        if len(subset) == N and sum(subset) == K:
            res += 1

    print(f'#{tc} {res}')