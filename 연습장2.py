N = int(input())

steps = [0]

for _ in range(6):
    steps.append(int(input()))

Memo = [0]*(N+1)
calN2 = [False]*(N+1)

def Max(n):

    if n == 1:
        Memo[1] = steps[1]
        return Memo[1]
    elif n == 2:
        Memo[2] = steps[1] + steps[2]
        return Memo[2]
    elif n == 3:
        a = steps[1] + steps[2]
        b = steps[1] + steps[3]
        if a > b : 
            Memo[3] = a
            Memo[4] = True
        else:
            Memo[3] = b 
        return Memo[3]
    elif n >= 4:
        if Memo[n] != 0:
            return Memo[n]
        if calN2==True:
            Memo[n] = Max(n-2)+steps[n]
            return Memo[n]
        elif calN2==False:
            Memo[n] = max(Max(n-1), Max(n-2))+steps[n]
            calN2[n+1] = True
            return Memo[n]


print(Max(N))