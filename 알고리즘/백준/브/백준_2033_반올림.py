import math   

N = int(input())    # 4666
length=len(str(N))  # 4 
cnt=0

def R(N,d):
    """
    N을 10의 d승까지 반올림하여 반환해주는 함수
    """
    #print(N/(10**d))
    N= math.floor(((N/(10**d))+0.5)) 
    #print(N)
    N= N*(10**d)
    return N 

 
for i in range(1,length):
    N=R(N,i)

print(N)