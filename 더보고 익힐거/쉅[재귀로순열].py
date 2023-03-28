p = [1,2,3]
N = len(p)

def f(i,k):
    if i == k:  # 세번째 항까지 모두 완성시켰으면 출력
        print(p)
    else:
        for j in range(i, k):       # 현재 취급하는 항의 오른쪽에있는항들이랑 위치 한번씩 다 바꿈.
            p[i],p[j]=p[j],p[i]
            f(i+1, k)
            p[i],p[j]=p[j],p[i]

f(0,N)

