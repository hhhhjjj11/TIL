N, M = map( int , input().split() )
li=[]
for _ in range(N):
    li.append(list(input()))

cnt=0
# 행부터 확인 
needcheck=0
for 행 in range(N):
# 만약 전부 비어있으면
    if li[행].count('.')==M:
         # Q. 반복문 안에서 해야할일인가 아니면 따로 확인해야할 일인가 ,를 판단하는 기준??
        # print(f'{행}번째 행 경비없음.')
        for 열 in range(M):
            colcheck=1
            for 행2 in range(N):
                if li[행2][열] !='.':
                    colcheck=0
            if colcheck==1:
                li[행][열]='X'
                cnt+=1
                break

for i in range(N):
    if li[i].count('.')==M:
        cnt+=1

for j in range(M):
    isthereGuard=False
    for i in range(N):
        if li[i][j] != '.':
            isthereGuard=True
    if isthereGuard==False:
        cnt+=1
           
print(cnt)
# 열 확인
# 열도 전부 비어있따  -> x로 바꾸고 cnt+=1 
# 아니면 패스

# 이렇게 다 돌면

# 빈 행 또는 빈 열 있는 지 확인.
# 빈 행 , 빈 열 수 만큼 cnt에 더해줌

# return(cnt)