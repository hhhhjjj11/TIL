# 일단 
# 0~4까지 리스트 만들어
# 합집합 한다 -> 대표원소를 가르키게 해주면 됨.

# 대표원소가 같다 <-> 같은 집합이다 의미로 사용

# 참고 같은팀이 되기 싫어하는 경우는 완전 다른 문제라는것 알고있자. 완전 다른 알고리즘을 써야함.. (색칠하기문제임)

def findrep(i):
    #print('findrep','i',i)
    if rep[i] == i:
        return i
    else:
        rep[i] = findrep(rep[i])
        return rep[i]
    
def union(i,j):
    rep_num = findrep(i)
    rep[j] = rep_num

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    li = list(map(int,input().split()))
    
    #print('li',li)
    rep = list(range(N+1))

    rep[0] = 'X'
    
    for i in range(M):
        a, b = min(li[2*i], li[2*i+1]), max(li[2*i], li[2*i+1])
        union(a,b)
    
    #print('rep',rep)
    res = 0
    for i in range(N+1):
        if rep[i] == i:
            res +=1 
    print(f'#{tc} {res}')