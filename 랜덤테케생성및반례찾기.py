from random import randint

# 예제 생성
def example():
    N = randint(1,15)
    r = randint(0,2**N-1)
    c = randint(0,2**N-1)
    
    return [N,r,c]

# 맞은 답
def right_sol(N,r,c):

    ans = 0

    while N != 0:

        N -= 1

        # 1사분면
        if r < 2 ** N and c < 2 ** N:
            ans += ( 2 ** N ) * ( 2 ** N ) * 0

        # 2사분면
        elif r < 2 ** N and c >= 2 ** N: 
            ans += ( 2 ** N ) * ( 2 ** N ) * 1
            c -= ( 2 ** N )
            
        # 3사분면    
        elif r >= 2 ** N and c < 2 ** N: 
            ans += ( 2 ** N ) * ( 2 ** N ) * 2
            r -= ( 2 ** N )
            
        # 4사분면    
        else:
            ans += ( 2 ** N ) * ( 2 ** N ) * 3
            r -= ( 2 ** N )
            c -= ( 2 ** N )
        
    return ans

# 틀린 답
def wrong_sol(N,r,c):

    # 분자와 분모를 각각 소인수 분해한다.  -> 숫자 너무 커서 소인수분해 에바임 네개의 숫자를 각각 소인수 분해한다음 
    # 소인수분해한 리스트를 이용하는 방식으로 해야 시간초과 안남

    # 철저히 소인수분해한 리스트를 이용한다. 
    # 곱하는것은 마지막에 한다.

    ans = 0 
    size = 2 ** N
    while size != 0:
        # 1구역
        if 0 <= r < size//2 and 0 <= c < size//2:
            pass
        # 2구역
        elif 0 < r < size//2 and size//2 <= c < size:
            ans += (size//2)**2 * 1
            c -= size//2
        # 3구역
        elif size//2 <= r < size and 0 < c < size//2:
            ans += (size//2)**2 * 2
            r -= size//2
        # 4구역
        else:
            ans += (size//2)**2 * 3
            r -= size//2
            c -= size//2
        size//= 2
        
    return ans

# 반례 출력
def check():
	ex = example()
	right = right_sol(ex[0], ex[1], ex[2])
	wrong = wrong_sol(ex[0], ex[1], ex[2])
	if right != wrong:
		print(ex[0], ex[1],ex[2])

		print("맞은 답:", right)
		print("틀린 답:", wrong)
		return
	else:
		check()

check()