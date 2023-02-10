import sys
input = sys.stdin.readline

n = int(input().strip())

li = [0,1,2,3]


def tile(n):
    if n <= 3:
        return li[n]
    return tile(n-1)+tile(n-2)

print(tile(n)%10007)