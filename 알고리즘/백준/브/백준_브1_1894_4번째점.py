import math
import traceback

while True:
    try:
        xx=list(map(float, input().split())) 

        li=[]
        for i in range(4):
            l=[]
            for j in range(2):
                l.append((xx[2*i+j]))
            li.append(l)

        common_point = 0

        for i in range(len(li)-1):
            for j in range(i+1, len(li)):
                if li[i]==li[j] :
                    common_point=li[i]
                    break
            if common_point:
                break
        
        while common_point  in li:
            li.remove(common_point)

        sumX=0
        sumY=0


        for i in li:
            sumX+=i[0]
            sumY+=i[1]

        X = sumX-common_point[0]
        Y = sumY-common_point[1]
        
        X= round(X,3)
        Y= round(Y,3)

        # X=math.trunc(1000*X)/1000 
        # Y=math.trunc(1000*Y)/1000 

        print(f'{X :.3f}',f'{Y :.3f}')
    except Exception as e:
        break
     

