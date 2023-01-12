T = int(input())
for i in range(T):
    t=int(input())
    li=list(map(int,input().split()))
    countli=list(range(101))
    for j in range(101):
        countli[j]=0
    for k in range(1000):
        countli[li[k]]+=1
    x=0
    y=0
    for l in range(100):
        if x<=countli[l]:
            x=countli[l]
            y=l
    print(f'#{i+1} {y}')




# sol 2, list.count메서드 사용
T = int(input())
for t in range(1,T+1):
    tc=int(input())
    li=list(map(int,input().split()))
    A=0
    for i in range(1000):
        if arr.count(j) >= arr.count(A):
            A=j
    print(f'#{t} {A}')