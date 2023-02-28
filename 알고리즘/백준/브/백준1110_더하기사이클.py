N=int(input())
N2=N 
cnt=0

while True:
    십의자리=N2%10
    일의자리=N2//10+N2%10
    일의자리=일의자리%10
    N2=십의자리*10+일의자리
    cnt+=1
    if N2==N:
        break
print(cnt)
