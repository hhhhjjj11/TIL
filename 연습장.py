N, L = map(int,input().split())

def sol(N,L):
    if (N-L) % L == 0:
        return list(range((N-L)//L,(N-L)//L + L))
    else:
        sol(N,L+1)


print(sol(N,L))




