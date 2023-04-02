from random import randint

# 예제 생성
def example():
	A1 = randint(1, 30000)
	B1 = randint(1, 30000)
	A2 = randint(1, 30000)
	B2 = randint(1, 30000)
	
	return [A1,B1,A2,B2]

# 맞은 답
def right_sol(A,B,C,D):
    def gcd(x,y): #최대공약수, 유클리드 호제
        mod = x % y
        while mod >0:
            x = y
            y = mod
            mod = x % y
        return y    

    N = gcd(A*D + C*B, B*D) 
    res = ((A*D + C*B)//N, B*D//N)
    return res

# 틀린 답
def wrong_sol(A1,B1,A2,B2):

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

    bonja.append(exception1+exception2)

    #print('bonja',bonja)
    #print('bonmo', bonmo)

    commons_final = GCDlist(bonja,bonmo)

    #print('coomons_final',commons_final)

    for common in commons_final:
        bonja.remove(common)
        bonmo.remove(common)

    res1, res2 = 1,1

    for x in bonja:
        res1 *= x
    for x in bonmo:
        res2 *= x

    RES = (res1,res2)
    return RES

# 반례 출력
def check():
	ex = example()
	right = right_sol(ex[0], ex[1], ex[2],ex[3])
	wrong = wrong_sol(ex[0], ex[1], ex[2],ex[3])
	if right != wrong:
		print(ex[0], ex[1],ex[2],ex[3])

		print("맞은 답:", right)
		print("틀린 답:", wrong)
		return
	else:
		check()

check()