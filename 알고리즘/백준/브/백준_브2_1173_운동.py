import sys
sys.setrecursionlimit(10**5)

N,m,M,T,R = map(int,input().split())


a=m
T_total = 0
T_work = 0
x=1

def HMNT(X):

    if m+T>M:
        print(-1)
        return
    global a
    global T_work
    global T_total
    맥박_운동후=a+T
    맥박_휴식후=a-R    
    if 맥박_운동후 > M: #휴식해야함
        T_total += 1
        if 맥박_휴식후<m:
            a=m
        else:
            a=맥박_휴식후
#        print('휴식함,', '맥박 :',a, 'total',T_total )
    else:                   # 운동 ㄱㄱ
        T_total += 1
        T_work += 1
        a=맥박_운동후
#        print('운동함,', '맥박 : ',a, 'total',T_total)

    if T_work ==X:             # 운동시간이 X와 같아지면 운동그만
        print(T_total)
        return
    HMNT(N)

HMNT(N)