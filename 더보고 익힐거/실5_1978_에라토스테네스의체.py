N = int(input())
inputs = list(map(int,input().split()))

res = 0

def isPrime(n):                 # n = 15
    if n <= 1 :
        return False
    
    li = [True]*(n+1)   # [1,2,3, ,,, , 15]
    for i in range(2,n+1):    # index+1 = num 
        m=2
        while True:
            if i*m>n:
                break
            li[i*m] = False
            m+=1
    
    return li[n]

for item in inputs:
    if isPrime(item):
        res+=1

print(res)


# 알아두기 1. 인덱스를 값으로 이용. i.e. 인덱스가 곧 값인 리스트를 이용. (0부터 1씩 증가하는 수열)
#               그러기위해서는 n+1개의 항을 만들어야 됨.!!
