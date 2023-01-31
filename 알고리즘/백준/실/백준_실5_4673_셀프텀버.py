def is_selfnumber(n):
    if n<=100:
        for i in range(1,n+1):
            res=i
            n2=i
            while n2>0:
                res+=n2%10
                n2=n2//10
            if res == n:
                return
        return print(n)
    elif 100<n<1000:    
        for i in range(n-30,n+1):
            res=i
            n2=i
            while n2>0:
                res+=n2%10
                n2=n2//10
            if res == n:
                return
        return print(n)
    elif 1000<n<=10000:
        for i in range(n-40,n+1):
            res=i
            n2=i
            while n2>0:
                res+=n2%10
                n2=n2//10
            if res == n:
                return
        return print(n)            
    


for i in range(1,10001):
    is_selfnumber(i)