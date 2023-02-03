N ,M = map(int,input().split())

NO =[[]]*201
print('NO', NO)
for _ in range(M):
    p,q = map(int,input().split())
    mm = min([q,p])
    MM = max([q,p])
    print('p,q :',p,q,'m,M :',mm,MM)
    NO[mm].append(MM)
    print(NO[mm])
    

print('NO',NO)
res = []

for i in range(1, N+1):
    for j in range(i+1, N+1):
        for k in range(j+1, N+1):
            res.append({i,j,k})

cnt=0

for i in range(len(res)):  # 결과들 모아놓은것
    isRight=True
    for j, li in enumerate(NO):  # 금지조합의 인덱스와 각항
        for v in li:
            print('j,v',{j,v})
            if len(res[i]-{j,v}) ==1 :
                isRight=False    
            if isRight==False:
                break
        if isRight==False:
            break
    if isRight==False:
        continue
    else:
        cnt+=1
        
print(cnt)

# 풀이 알아두기 . 수학문제 풀듯 푸는거 아니다. 
# 선형계산이 최고다..