N = int(input())

li = list(map(int,input().split()))

nowIdx = 0
res = [1] 
while len(res)<N :
    move = li[nowIdx%N]
    #print('move',move)
    li[nowIdx%N]='X'
    
    if move > 0:
        while move>0:
            #print('move',move)
            if li[(nowIdx+1)%N] != 'X':
                nowIdx += 1
                move-=1
            else:
                nowIdx += 1
        res.append(nowIdx%N+1)
        #print(nowIdx%N+1)
    elif move < 0 :
        while move<0:
            #print('move',move)
            if li[(nowIdx-1)%N] != 'X':
                nowIdx -=1
                move +=1
            else:
                nowIdx -=1
        res.append(nowIdx%N+1)
        #print(nowIdx%N+1)

res = list(map(str,res))
print(' '.join(res))