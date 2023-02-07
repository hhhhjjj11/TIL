
#for tc in range(1,11):
n = int(input())
res = 0
li =[]
for i in range(100):
    li.append(list(map(int,input().split())))

# 2의 위치 (출발점)
for i in range(100):
    for j in range(100):
        if li[i][j] == 2:
            x,y= i,j

while True:
    #print('now', x,y)
    if x<=0:
        break
    if  0<y+1<100 and li[x][y+1] ==1:
        y = y+1
    elif 0<y-1<100 and li[x][y-1] ==1:
        y = y -1
    else:
        x = x-1

print(f'#{n} {y}')