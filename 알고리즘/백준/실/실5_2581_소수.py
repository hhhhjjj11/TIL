M = int(input())
N = int(input())

def get_Prime_less_than(n):               
    if n <= 1 :
        return []
    
    li = [True]*(n+1)   
    for i in range(2,n+1):    
        m=2
        while True:
            if i*m>n:
                break
            li[i*m] = False
            m+=1
    
    res= []
    for i in range(1,len(li)):
        if li[i]==True:
            res.append(i)
            
    return res

M=get_Prime_less_than(M-1)
# print(M)
N=get_Prime_less_than(N)
if 1 in N:
    N.remove(1)
#print(N)
s1 = set(M)
s2 = set(N)

#print('s1',s1,'s2',s2)
s = s2 - s1

results = list(s)
#print (results)
if len(results) == 0 :
    print(-1)
else:
    print(sum(results))
    print(min(results))