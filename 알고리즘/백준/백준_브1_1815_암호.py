col = int(input())
enc=input()
row = int(len(enc)/col)
li=[]
for i in range(row):
    l=[]
    if i % 2 == 0:
        for j in range(col):
            l.append(enc[col*i+j])
    if i % 2 == 1:
        for j in range(col):
            l.append(enc[(i+1)*col-(j+1)])
    li.append(l)

res=[]

for c in range(col):
    for r in range(row):
        res.append(li[r][c]) 

print(''.join(res))
