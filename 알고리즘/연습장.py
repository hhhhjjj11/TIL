from sys import stdin

N, K = map(int,input().split())

coin=[]
for _ in range(N):
    coin.append(int(stdin.readline().rstrip()))

cnt =0
for i in range(len(coin)-1,-1,-1):
    while K>=coin[i]:
        K-=coin[i]
        cnt+=1
    if K ==0:
        break

print(cnt)
