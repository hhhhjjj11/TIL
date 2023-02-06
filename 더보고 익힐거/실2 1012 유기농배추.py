from pprint import pprint

T = int(input())

# 2차원 배열에서, 주변의 특정값과 인접한 덩어리를 전부 C로바꿔주기

def contagious(i,j):

    li[i][j] ='C'

    주변 =[]
    try :
        if li[i+1][j]:
            주변.append((i+1,j))
    except:
        pass
    try :
        if li[i-1][j] and i>0:
            주변.append((i-1,j))
    except:
        pass
    try :
        if li[i][j+1]:
            주변.append((i,j+1))
    except:
        pass
    try :
        if li[i][j-1] and j>0:
            주변.append((i,j-1))
    except:
        pass

    주변배추=[]
    
    for 좌표 in 주변:
        행,열 = 좌표
        if li[행][열] == 1:
            li[행][열] = 'C'
            주변배추.append(좌표)

    if len(주변배추)==0:
        return

    for 배추좌표 in 주변배추:
        행,열 = 배추좌표
        li[행][열] = 'C'
        contagious(행,열)


for tc in range(T):
    N,M,K=map(int,input().split())

    li =[]

    for i in range(M):
        tem=[0]*N
        li.append(tem)

    for _ in range(K):
        i,j=map(int,input().split())
        li[j][i] = 1

    cnt = 0

    for i in range(M):
        for j in range(N):
            if li[i][j] == 1:
                contagious(i,j)
                #pprint(li)
                cnt+=1

    print(cnt)

