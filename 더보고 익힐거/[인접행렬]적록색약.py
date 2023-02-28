import sys
sys.setrecursionlimit(100000)

import copy 
input = sys.stdin.readline

N = int(input().strip())

li = [list(input().strip()) for _ in range(N)]

li2 = copy.deepcopy(li)

def contagious(i,j):

    #print(f'현재{i,j}항, {Clrnow}색')
    li[i][j] = 'CHECK' # 확인표시로 바꿔주고

    aroundIdx= [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] # 상하좌우 (인접배열)
    
    aroundIdx_corresponding = [] 

    # 인접 항들을 확인해서 같은 색상인 애들 따로 담아주기
    for idx in aroundIdx:
        x,y = idx
        if 0<=x<=N-1 and 0<=y<=N-1 and li[x][y] == Clrnow:
            aroundIdx_corresponding.append((x,y))
            #print('해당주변', aroundIdx_corresponding)

    if len(aroundIdx_corresponding) == 0:
        return

    for idx in aroundIdx_corresponding:
        x,y = idx
        contagious(x,y)        
       




def RG(i,j):

    #print('i, j :',i,j)
    li[i][j] = 'CHECK' # 확인표시로 바꿔주고

    #print(li)
    aroundIdx= [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] # 상하좌우 (인접배열)

    aroundIdx_corresponding = [] 

    # 인접 항들을 확인해서 같은 색상인 애들 따로 담아주기
    for idx in aroundIdx:
        x,y = idx
        if 0<=x<=N-1 and 0<=y<=N-1 and (li[x][y]=='R' or li[x][y]=='G'):
            aroundIdx_corresponding.append((x,y))
            #print('해당주변', aroundIdx_corresponding)

    if len(aroundIdx_corresponding) == 0:
        return

    for idx in aroundIdx_corresponding:
        x,y = idx
        RG(x,y)        



# 적록색약 
cnt1=0
for i in range(N):
    for j in range(N):
        #print(i,j)
        #print('cnt1',cnt1)
        if li[i][j] == 'CHECK':
            continue
        elif li[i][j] == 'B':
            Clrnow='B'
            contagious(i,j)
            cnt1+=1
        elif li[i][j]=='R' or li[i][j]=='G':
            
            RG(i,j)
            cnt1+=1


# 정상
cnt2=0
li = li2
#print(li)
for i in range(N):
    for j in range(N):
        if li2[i][j] == 'CHECK':
            continue
        Clrnow=li[i][j]
        contagious(i,j)
        cnt2+=1 

print(cnt2,cnt1)

            
                                        
            