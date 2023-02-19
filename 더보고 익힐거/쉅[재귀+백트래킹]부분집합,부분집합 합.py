# 부분집합 비트 만들기

def f(i,k):
    if i ==k:
        print(bit)
    else:
        bit[i] = 1
        f(i+1,k)
        bit[i] = 0
        f(i+1 ,k)
    
bit =[0,0,0,0]

f(0,4)

# 부분집합 비트를이용해서 부분집합 만들기

def f(i,k):
    if i ==k:    
        for j in range(k):
            if bit[j]:
                print(A[j], end=' ')
        print(bit)
    else:
        bit[i] = 1
        f(i+1,k)
        bit[i] = 0
        f(i+1 ,k)
    
bit =[0,0,0,0]
A = [1,2,3,4]

f(0,4)

# 부분집합 합 구하기

def f(i,k):
    if i ==k:
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
                print(A[j], end=' ')
        print(bit, s)
    else:
        bit[i] = 1
        f(i+1,k)
        bit[i] = 0
        f(i+1 ,k)
    
bit =[0,0,0,0]
A = [1,2,3,4]

f(0,4)

# 예제 : 부분집합의 합이 10인 경우 찾으세요
A = [1,2,3,4,5,6,7,8,9,10]

def f(i,k):
    if i == k:    # 끝까지 갓으면. (개수 다 채웠으면) (부분집합 완성임.)
        s = 0
        temp = []
        for j in range(k):
            if bit[j]:
                s += A[j]
                temp.append(A[j])
        if s == 10:
            print('합 10',temp)
    else:
        bit[i] = 1
        f(i+1,k)
        bit[i] = 0  
        f(i+1 ,k)

bit = [0]*10
f(0,10)

def f(i,k,key):
    if i ==k:    # 끝까지 갓으면. (개수 다 채웠으면) (부분집합 완성임.)
        s = 0
        temp = []
        for j in range(k):
            if bit[j]:
                s += A[j]
                temp.append(A[j])
        if s == key:
            print('합 10',temp)
    else:
        bit[i] = 1
        f(i+1,k, key)
        bit[i] = 0
        f(i+1 ,k, key)

bit = [0]*10
f(0,10,10)


# 원소의 합이 10인 부분집합의 개수 구하기
# (백트래킹 섞으면 더 효율적으로 찾을 수 있다. 일단은 백트래킹없이.) 
# (부분집합들의 합들을 구하다가 10을 넘으면 탐색중지.)
# 원소의 합이 10인지 아닌지만 보면 되므 비트를 이용할 필요도 없음. 

def f(i,k,s,t): # i 원소, k집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt
    if i == k :
        if s ==t :
            cnt+=1
        return
    else:  
        f(i+1, k, s+A[i], t)    # A[i] 포함
        f(i+1, k, s, t)         # A[i] 미포함


A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 12
cnt = 0 
bit = [0]*N

f(0,N,0,key)
print(cnt)


# 원소의 합이 KEY인 부분집합을 모두 구해보면 (다시 비트를이용)

def f(i,k,s,t): # i 원소, k집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt
    global fcnt
    fcnt += 1 # 재귀함수가 몇번 호출되 었는지 파악할 수 있음.
    if i == k :
        if s == t :
            for j in range(k):          # 요부분 추가해서 찍어주면 됨.
                if bit[j] :
                    print(A[j], end=' ')
            print()
            cnt+=1
        return
    else:  
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함

fcnt = 0
A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 12
cnt = 0 
bit = [0]*N

f(0,N,0,key)
print(cnt, fcnt)  # 13, 2047 // 합이 key인경우의 수 = 13 이고 답을 찾기위해 함수를 2047번 호출했다는 의미.


# 자, 우리의 목표. 백트래킹을 이용해서 답을 찾아보자 
# 별거 없음, 이미 답이 아닌경우로 판명 된 케이스의 경우 더이상 탐색하지 않도록 조건을 추가해 주는 것이 백트래킹임.
# 이 문제의 경우, s가 이미 key보다 클 경우 더이상 탐색을 하지 않아도 됨.
# 따라서 해당 조건을 함수 본문에 추가시켜주면 끝임.

def f(i,k,s,t): # i 원소, k집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt
    global fcnt
    fcnt += 1 # 재귀함수가 몇번 호출되 었는지 파악할 수 있음.
    if s > t :  # 고려한 원소의 합이 찾는 합보다 큰 경우
        return 
    if i == k : # 끝까지 간 경우.
        if s == t :
            for j in range(k):          # 요부분 추가해서 찍어주면 됨.
                if bit[j] :
                    print(A[j], end=' ')
            print()
            cnt+=1
        return
    else:  
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함

fcnt = 0
A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 12
cnt = 0 
bit = [0]*N
f(0,N,0,key)
print(cnt, fcnt)   # 13 555 // 탐색횟수가 1/4로 줄어듦. 개꿀.


# 다음과 같이 조건을 추가하면, 더 효율적으로 찾을 수도 있다. 재귀호출횟수를 더 줄일 수도 있다. 
def f(i,k,s,t): # i 원소, k집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt
    global fcnt
    fcnt += 1 # 재귀함수가 몇번 호출되 었는지 파악할 수 있음.
    if s > t :  # 고려한 원소의 합이 찾는 합보다 큰 경우
        return 
    elif s == t: # 남은 원소 고려할 필요 X
        cnt += 1
        return
    elif i == k : # 모든 원소 고려
        return
    else:  
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함


# 참고. 다음의 경우를 생각해보자.
A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 55

# 이 경우 DFS를 사용했을때의 호출횟수와 백트래킹을 적용한경우랑 차이가 없음. 전부 끝까지 돌아야 하기 때문에.
# 따라서 이런 경우 호출횟수를 줄이려면 또 적절한 조건을 추가해야 함.
# "백트래킹은 대체로 좋아지지만 최악의 경우 DFS로 다돌린 것과 똑같다"

# 다음과 같은 조건을 추가하면 위와 같은 문제를 개선할 수있음.
# -> 남은 원소의 합을 다 더해도 찾는 값 T보다 작을 경우 탐색 중단.