M,N = map(int,input().split())

li=[]
for _ in range(M):
    li.append(list(map(int,input().split())))

# print(li)
T = int(input())
for _ in range(T):
    i,j,x,y=map(int,input().split()) # 1 1 2 3
    i = i-1
    j = j-1
    x = x-1
    y = y-1
    # 0 0 1 2
    total =0

    for 행 in range(i,x+1):
        pass
        total += sum(li[행][:y+1])-sum(li[행][:j])               

    print(total)
