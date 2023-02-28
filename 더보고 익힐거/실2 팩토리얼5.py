# 알아두기 적당히 존나큰 수 이용한다. 

N = int(input())

def fact5(N):
    res = 1
    while N>0:
        res *= N
        while res%10 ==0:
            res//=10
        #print(res)
        res%=10**15
        N -= 1
        
    return str(res)[-5:]

print(fact5(N))
#print(fact(N))

