N = int(input())

# 만약 다른 함수 다음 문자열이

def isGroup(S):
    res = True
    n=0
    if len(S) == 1:
        return True
    while True :
        if n == len(S)-1:
            break
       
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
       
    return res

cnt=0
for t in range(N):
    a = input()
    if isGroup(a) == True :
        cnt+=1

print(cnt)