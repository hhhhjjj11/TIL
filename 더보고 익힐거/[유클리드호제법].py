# 분수 두개 입력받아서 두 분수의 합을 기약분수꼴로 출력하기


# 정답코드
def gcd(x,y): #최대공약수, 유클리드 호제
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y    

A, B = map(int, input().split())
C, D = map(int, input().split())
N = gcd(A*D + C*B, B*D) 
print((A*D + C*B)//N, B*D//N)


# 내가 푼 코드(틀림)
# 이유 -> 
# exception1+exception2도 소인수 분해 해줘야하는거 놓쳤었음.
# 근데 소인수분해 할라해도 그게 얼마나 클지모름. 많이 크면 안돌아감..

A1, B1 = map(int,input().split())
A2, B2 = map(int,input().split())


# 분자와 분모를 각각 소인수 분해한다.  -> 숫자 너무 커서 소인수분해 에바임 네개의 숫자를 각각 소인수 분해한다음 
# 소인수분해한 리스트를 이용하는 방식으로 해야 시간초과 안남

# 철저히 소인수분해한 리스트를 이용한다. 
# 곱하는것은 마지막에 한다.


def factorization(N):
    result =[]

    for div in range(2,N+1):
        if N%div == 0:
            while N%div == 0:
                result.append(div)
                N //= div

    return result

def GCDlist(li1,li2):
    commons = []
    check = [0]*len(li2)
    for i in range(len(li1)):
        for j in range(len(li2)):
            x1,x2 = li1[i],li2[j]
            if x1 == x2 and not check[j]:
                check[j] = 1
                commons.append(x1)
                break
    return commons

def LCDlist(li1,li2):
    gcdlist = GCDlist(li1,li2)
    gcd= 1
    for x1 in gcdlist:
        gcd *= x1
    res = []
    # li1에서 gcd랑 안겹치는 애들 res에 담는다.
    # li2에서도 gcd랑 안겹치는 애들 res에 담는다.
    a = 1
    for x1 in li1:
        a*=1
    a = a//gcd
    for x1 in factorization(a):
        res.append(x1)
    b=1
    for x2 in li2:
        b *=x2
    b = b//gcd
    for x2 in factorization(b):
        res.append(x2)
    for x1 in gcdlist:
        res.append(x1)
    res.sort()
    return res

a1 = factorization(A1)
b1 = factorization(B1)
a2 = factorization(A2)
b2 = factorization(B2)

#print('!', a1,a2,b1,b2)

# 네개의 숫자를 각각 소인수 분해  

# 통분 (B1,B2의 최소공배수)  
# -> 굳이 통분안하는게 더 효율적일 수도 있을것같다. 통분하는데 필요한 계산과정 생략가능하므로.
bonmo = []
for x in b1:
    bonmo.append(x)
for x in b2:
    bonmo.append(x)

#print('분모계산완료')

# 분자구하기
# A1*B2 + A2*B1
temp1 = []
temp2 = []

for a in a1:
    temp1.append(a)
for b in b2:
    temp1.append(b)

for a in a2:
    temp2.append(a)
for b in b1:
    temp2.append(b)

#print('tem1,tem2',temp1,temp2)

gcdlist = GCDlist(temp1,temp2)
#print('temp1과 temp2의 gcd',gcdlist)
bonja = []

for common_divisor in gcdlist:
    bonja.append(common_divisor)
    if common_divisor in temp1:
        temp1.remove(common_divisor)
    if common_divisor in temp2:
        temp2.remove(common_divisor)

exception1 = 1
exception2 = 1
#print('공통부분 지운이후 temp',temp1,temp2)
for x in temp1:
    exception1 *= x
for x in temp2:
    exception2 *= x

# 이렇게 하면 이거 더한다음에 factorization하는게 안된다.....
# 유클리드 호제법 써야한다..
XX = factorization(exception1+exception2)
for xx in XX:
    bonja.append(xx)

print('bonja',bonja)
print('bonmo', bonmo)

commons_final = GCDlist(bonja,bonmo)

print('coomons_final',commons_final)

for common in commons_final:
    bonja.remove(common)
    bonmo.remove(common)

res1, res2 = 1,1

for x in bonja:
    res1 *= x
for x in bonmo:
    res2 *= x

print(res1,res2)