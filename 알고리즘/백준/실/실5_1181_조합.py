T = int(input())


def factorial(n):
    if n == 0 :
        return 1
    res = 1
    while 1:
        if n ==1:
            break
        res= res*n
        n-=1

    return res

def Combination(n,r):
    n_fac = factorial(n)
    #print('nfac',n_fac)
    r_fac = factorial(r)
    #print('rfac',r_fac)
    n_minus_r_fac=factorial(n-r)
    #print('n_minus_r_fac',n_minus_r_fac)
    
    return int(n_fac / (n_minus_r_fac * r_fac))

for t in range(T):
    N, M =map(int,input().split())
    print(Combination(M,N))

