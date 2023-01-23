# 학생수

N = int(input())

li=[] # key가 한개면 list에 담고 key가 여러개면 li안의 dic에 담자.
count=[]
for student in range(N):
    li.append(list(map(int,input().split())))

#print(li)

for i in range(N):  # i 는 학생순번임.
    dic={}
    for j in range(5):
        for k in range(N):
            if li[k][j]==li[i][j]:
                dic[k+1]=dic.get(k+1,0)+1
    count.append(dic)

#print(count)
keycount=[]
for item in count:
    keycount.append(len(item.keys()))

result=keycount.index(max(keycount))+1
print(result)