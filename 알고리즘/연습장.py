# print(input().split())
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
            if li[i]==li[i+1] :
                common_point=li[i]
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

        X=round(X,3)
        Y=round(Y,3)



        print(f'{X:.3f} {Y:.3f}')
    except:
        break