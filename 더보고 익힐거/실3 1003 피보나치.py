from sys import stdin


# def fibo(n):

#     if n==0:
#         return 0
#     elif n ==1 :
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

def fibo2(n):
    if n <= 0 :
        return 0
    cnt =2
    a1 = 1
    a2 = 1
    res= [a1,a2]
    while cnt <n:
        a3 = a1+a2
        res.append(a3)
        cnt+=1
        a1 = a2
        a2 = a3
    return res[n-1]


T = int(stdin.readline().rstrip())

for tc in range(T):

    n = int(stdin.readline().rstrip())
    if n ==0:
        print(1, 0)
    else:
        print(fibo2(n-1),fibo2(n))


# 알아두기 1. 피보나치 주석단것 처럼 재귀로 짜면 시간초과 에바임 걍 fibo2로 쓰는게 나은듯.
# 알아두기 2. 피보나치 주단것처럼 할 경우 이유는 모르겠는데 fibo(n)실행시 0나오는 횟수는 fibo(n-1)과 같음.