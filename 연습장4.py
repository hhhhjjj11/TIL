N = int(input())

initial = [list(map(int,input().split())) for _ in range(N)]

cnt1 = 0
cnt2 = 0
cnt3 = 0

stack=[initial]

while stack:
    paper = stack.pop()
    N = len(paper)
    s=set()
    for i in range(N):
        for j in range(N):
            s.add(paper[i][j])
            if len(s)>1:
                break   
        if len(s)>1:
            break
    if len(s) ==1:
        if paper[0][0] == 1:
            cnt1 += 1
        elif paper[0][0] == 0:
            cnt2 +=1
        elif paper[0][0] == -1:
            cnt3 +=1
    else: 
        N//=3
        if N >1:
            for i in range(3):
                for j in range(3):
                    temp=[]
                    for k in range(N):
                        temprow=[]
                        for l in range(N):
                            temprow.append(paper[3*i+k][3*j+l])
                        temp.append(temprow)
                    stack.append(temp)
        else:
            for i in range(3):
                for j in range(3):
                    if paper[i][j] == 1:
                        cnt1 +=1
                    elif paper[i][j] == 0:
                        cnt2 +=1
                    elif paper[i][j] == -1:
                        cnt3 += 1

print(cnt3)
print(cnt2)
print(cnt1)