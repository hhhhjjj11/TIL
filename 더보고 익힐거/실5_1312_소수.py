A,B,N = map(int, input().split())
 
for i in range(N) :
    A = (A%B)*10
    result = A//B
 
print(result)





# 알아두기 파이썬은 소수점 아래 15째 자리까지만 나타내므로 순환소수의 자리수를 알아낼 수 없음.
# 따라서 단순히 나누고 그 중에서 문자열을 고르는 방식으로는 이 문제를해결할 수없음.

# 틀린코드
# import math

# A, B, N = map(int,input().split())

# # print((A/B))
# # print((A/B)*(10**N))
# # print(str(math.floor((A/B)*(10**N))))
# print(str(math.floor((A/B)*(10**N)))[-1])   