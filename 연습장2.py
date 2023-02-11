import sys
input = sys.stdin.readline

n = int(input().strip())

li = [0,1,2,3]
for _ in range(997):
    li.append(0)

def tile(n):
    if li[n] != 0:
        return li[n]
    else:
        li[n] = tile(n-1) + tile(n-2)
        return li[n]

print(tile(n)%10007)