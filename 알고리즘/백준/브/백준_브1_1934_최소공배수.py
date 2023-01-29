from sys import stdin

def gcd(a,b):
    m = min((a,b))
    M = max((a,b))
    for i in range(m):
        if M%(m-i) == 0 and m%(m-i)==0:
            return m-i



T = int(stdin.readline())
for _ in range(T):
    A,B = map(int,stdin.readline().split())
    
    print(int((A*B)/gcd(A,B)))