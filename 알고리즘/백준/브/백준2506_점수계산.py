N = int(input())
li = list(map(int,input().split()))

score=0

if li[0]==1:
    score+=1

n=1

for i in range(1,N):
    if li[i]==1:
        if li[i-1]==0:
            score+=n
        elif li[i-1]==1:
            n+=1
            score+=n
    else:
        n=1
        
print(score)
