N = int(input())

for _ in range(N):
    n = int(input())
    isKey=True
    for i in range(2,1000001):
        if n%i==0: 
            isKey=False
            break
    if isKey==True:
        print('YES')
    else: 
        print('NO')