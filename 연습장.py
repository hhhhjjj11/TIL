N = int(input())

step =[0]

for _ in range(N):
    step.append(int(input()))

Memo = [0]*(N+1)
now=0

while now<N:
    now += 1
    if now == 1:
        Memo[1] = step[1]
    if now == 2:
        Memo[2] = step[1] + step[2]
    if now == 3:
        Memo[3] = max(step[2],step[1]) + step[3]
    if now >= 4:
        Memo[now] = max(Memo[now-3]+step[now-1], Memo[now-2])+step[now] 

#print(Memo)
print(Memo[N])


    