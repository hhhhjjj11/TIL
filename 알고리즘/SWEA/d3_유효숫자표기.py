T = int(input())
for t in range(1,T+1):
    N=str(int(input()))
    n = list(N)
    
    #print('N', type(N),N)
    #print('n', type(n), n)
    자릿수=len(n)

    exceptional=True
    for i in range(자릿수):
        if int(n[i])!= 9:
            exceptional=False    

    나눌수=int(자릿수)-1
    a=1
    for _ in range(나눌수):
        a=a*10
    res = round(int(N)/a,1)
    res_exceptional= round(res/10,1)
    if exceptional==False:
        print(f'#{t} {res}*10^{나눌수}')
    else:
        print(f'#{t} {res_exceptional}*10^{나눌수+1}')