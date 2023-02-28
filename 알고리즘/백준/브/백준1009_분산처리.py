from sys import stdin

T = int(stdin.readline())
for t in range(T):
    a, b = map(int,stdin.readline().split())
    
    r1=a%10
    rests=[r1]
    X = r1
    while True:
        X=(X*a)%10
        
        if X==r1:
            break

        rests.append(X)

    length=len(rests)

    res = rests[b%length-1]
    if res==0:
        print(10)
    else:
        print(res)