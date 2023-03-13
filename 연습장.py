import sys
input = sys.stdin.readline

K, N  = map(int,input().split())

list = []
for _ in range(K):
    list.append(int(input()))

end = sum(list)//N

start = 1

while start<=end:
    mid = (start+end)//2
    X = 0
    for i in range(K):
        X += (list[i]//mid)
    if X>=N:
        start = mid+1
    else:
        end = mid -1

print(end)