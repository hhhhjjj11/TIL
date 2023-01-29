N = int(input())

def findnumber (X):
    if X == 1:
        return 0, 0
    n=0
    sum=0
    while True:
        sum+=n
        if sum > X:
            return n-1,sum-n    
        n+=1

a, sum2 = findnumber(N)
rest= N-sum2
if rest ==0:
    if a % 2 == 0:
        print(f'{a}/1')
    if a % 2 == 1:
        print(f'1/{a}')
elif a % 2 == 0:
    print(f'{a+2-rest}/{rest}')
elif a % 2 == 1:
    print(f'{rest}/{a+2-rest}')
