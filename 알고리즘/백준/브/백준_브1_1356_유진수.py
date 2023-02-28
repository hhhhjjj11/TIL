N = input()     # 1200012
l=len(N)        # 7
res='NO'  
for i in range(l-1):  # 0~5까지 i=2
    n1=1
    n2=1
    for j in range(l-i-1): #0,1,2,3  # 1,2,3,0
        n1 *= int(N[j]) 
    for j in range(i+1):  # 0,1,2  # 2,1,0
        n2 *= int(N[l-1-j])
    if n1==n2:
        res="YES"
        break
if res == 'YES':
    print(res)
else:
    print('NO')