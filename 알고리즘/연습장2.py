def isGroup(S):
    res = True
    n=0
    while True :
        
        if S[n] == S[n+1]:   # 만약 연속한 두항이 같으면 다음항따지기 
            n+=1
            continue
        else:
            for i in range(n+1,len(S)):
                if S[i]==S[n]:
                    res=False
                    break
        if res == False:
            break
        
        n+=1
        if n == len(S)-1:
            break

    return res


print(isGroup('aba'))
