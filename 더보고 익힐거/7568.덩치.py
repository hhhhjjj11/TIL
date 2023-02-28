N = int(input())
li = []
for _ in range(N):
    m,h=map(int,input().split())
    li.append([m,h])

for i, value in enumerate(li):
    li[i].append(i)


li = sorted(li, key = lambda x : x[0]and x[1], reverse=True)
# print(li)
for i, value in enumerate(li):
    rank=1
    for j in range(i):
        if li[i][0] <li[j][0] and li[i][1] < li[j][1]:
            rank+=1
    li[i].append(rank)

# print(li)
li = sorted(li, key = lambda x : x[2])

for item in li:
    print(item[3],end=' ')