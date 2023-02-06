import sys
sys.setrecursionlimit(10**9)

N, K = map(int,input().split())

d=[0]*(K+100) 


def f(K):

    if N == K :
        return 0

    elif N>K:

        if K==N+1:
            d[K]= 1
            return d[K]
        
        if d[K] != 0:
            return d[K]

        else : 
            #print(K)
            d[K] = f(K+1) + 1  
        
        return d[K]
        
    else: # K 가 더 큼.
 
        if K == 2*N or K==N+1:
            d[K]= 1
            return d[K]
        
        if d[K] != 0:
            return d[K]

        if K % 2 == 0:
            #print(K)
            if 1 in (f(K//2), f(K-1)):
                d[K] = 2
            else:
                d[K] = min(f(K//2), f(K-1)) + 1

        else : 
            #print(K)
            d[K] = f(K-1) + 1   # 
        
        return d[K]


print(f(K))

