memo = [0]* 252
memo[0] = 1
memo[1] = 1
memo[2] = 3

def sol(X):
    if memo[X] != 0:
        return memo[X]
    else:
        memo[X] = sol(X-1) + sol(X-2)*2 
        return memo[X]

while True:
    try:
        pass
        n = int(input())
        print(sol(n))
    except:
        break

