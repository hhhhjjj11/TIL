def collatz(N):

    cnt=0

    while True:
        if N==1:
            return cnt
        
        elif cnt==500:
            return -1

        else:
            if N % 2 == 0:
                N=N/2
                cnt+=1
            else:
                N=N*3 + 1
                cnt+=1

         

print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))