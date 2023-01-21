def fun(X):
    res=0
    cnt=0
    while True:
        if cnt == X:
            break
        for i in range(1,X+1):
            if cnt == X:
                break
            for _ in range(i):
                if cnt == X:
                    break
                res+=i
                cnt+=1
                print(res)
    return res

fun(3)
fun(7)
