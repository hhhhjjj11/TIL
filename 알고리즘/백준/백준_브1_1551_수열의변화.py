N, K = map(int,input().split())
li=list(map(int,input().split(',')))


while K>0:
    nli=[]
    for i in range(len(li)-1):
        nli.append(li[i+1]-li[i])

    li=nli
    K-=1

print(','.join(list(map(str,li))))