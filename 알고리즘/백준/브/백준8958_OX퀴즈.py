T = int(input())
for t in range(T):
    li = list(input())
    score=0
    length=len(li)
    n=1

    for i in range(length):
        if li[i]=='X':
            score+=0        
        elif li[i]=='O':
            if i==0:
                score+=1
            elif li[i-1]=='O':
                n+=1
                score+=n
            elif li[i-1]=='X':
                n=1
                score+=n
    print(score)