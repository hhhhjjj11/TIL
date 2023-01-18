N=int(input())   # 200
for i in range(1,N+1):
    li=list(str(i)) # [1,3,6]
    howMany369=0
    for j in range(len(li)): # 136 -> 3번반복
        #print(f'li[{i}]:', li[i])
        if li[j]=='3' or li[j]=='6' or li[j]=='9':  
            howMany369+=1  # 2
    #print('howmany369:',howMany369)
    if howMany369==0:
        print(i, end=' ')
    else:
        for _ in range(howMany369):
            print('-',end='')   # --
        print(' ',end='')
        

        
## 포문에서 i랑 j구분 못하면 i가 안읽히니까 에러조심
