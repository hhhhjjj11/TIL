T = int(input())

for tc in range(1,T+1):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    if r1 == 0 or r2 == 0 :
        print(1)
        continue
    if x1 == x2 and y1 ==y2: # 중심이 같을때 
        pass
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:        
        d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        if r1+r2 < d:
            print(0)
        elif r1 + r2 == d:
            print(1)
        else:
            # r1 + r2 > d
            M = max(r1,r2)
            m = min(r1,r2) 
            if M > m+d:
                print(0)
            elif M == m+d:
                print(1)
            else:
                print(2)