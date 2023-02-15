
N = int(input())

def fact5(N):
    res = 1
    while N>0:
        res *= N
        if list(str(res))[-1] == '0':
            res = list(str(res))
            res.pop()
            res= ''.join(res)
            res = int(res)
        if len(str(res))>5:
            res = str(res)[len(str(res))-5:]
            #print('res',res)
            res = int(res)
        #print(res)
        N -= 1
    if len(str(res))<5:
        add =''
        needZero = 5-len(str(res))
        for _ in range(needZero):
            add += '0'
        return add+str(res)
        
    return res

print(fact5(N))