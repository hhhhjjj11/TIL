T = int(input())

def isStartPointIn_C(cx,cy,r):
    
    d = ((cx-x1)**2 + (cy-y1)**2) ** (1/2)
    
    if d > r:
        return False 
    elif d < r:
        return True
       

def isEndPointIn_C(cx,cy,r):
    
    d = ((cx-x2)**2 + (cy-y2)**2) ** (1/2)
    
    if d > r:
        return False 
    elif d < r:
        return True
        

for tc in range(1,T+1):

    x1,y1,x2,y2 = map(int,input().split())
    
    n = int(input())

    cnt = 0

    for _ in range(n):
        cx,cy,r = map(int,input().split())

        #print(isStartPointIn_C(cx,cy,r),isEndPointIn_C(cx,cy,r)) 
        if not isStartPointIn_C(cx,cy,r) and isEndPointIn_C(cx,cy,r):  # 시작점은 원 안에 있고 도착점은 원 밖에있으면
            pass
            cnt+=1
        elif isStartPointIn_C(cx,cy,r) and not isEndPointIn_C(cx,cy,r):
            pass
            cnt +=1
    
    print(cnt)