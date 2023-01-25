# 재귀함수

n = 5

# n 번 째 자리의 피보나치 수 구하기
# 0 1 1 2 3 5 8 13 21 34 55 ... 
def fibo(n):
    # 종료 조건
    if n == 0 :
        return n
    elif n == 1 or n == 2 :
        return 1
    # 다음으로 넘어감
    # 최종적으로 우리가 return 받고자 하는 값을 생각하면 작성하기 쉽다
    return fibo(n-1) +  fibo(n-2)

print(fibo(n))


# n= 10
# 9 + 8
# 8+7 + 7+6
# 7 6 6 5 6 5 5 4 
# 6554544354434332