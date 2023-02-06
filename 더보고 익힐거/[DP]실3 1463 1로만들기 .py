X = int(input())

d = [0]*(X+1)  # 인덱스 = 숫자


def func(n):
    if n ==1 :
        return 0
    if n == 2:
        return 1
    if d[n] != 0: # 계산한 적이 있으면, 메모리에 저장 되어 있으면.
        return d[n]
    
    if n%6==0:
        d[n] = min(func(n//3)+1, func(n//2)+1)
    elif n % 3 == 0:
        d[n] = min(func(n-1)+1, func(n//3)+1) 
    elif n % 2 == 0:
        d[n] = min(func(n-1)+1, func(n//2)+1) 
    else:
        d[n]=func(n-1)+1

    return d[n]

print(func(X))




x=int(input())
dp={1:0}
def rec(n):
    if n in dp.keys():
        return dp[n]
    if n%6==0:
        dp[n]=min(rec(n//3)+1, rec(n//2)+1)
    elif n%3==0:
        dp[n]=min(rec(n//3)+1, rec(n-1)+1)
    elif n%2==0:
        dp[n]=min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n]=rec(n-1)+1
    return dp[n]
print(rec(x))