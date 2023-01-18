li=[0]*10
for i in range (10):
    li[i]=int(input())
dic={}
for i in range(10):
    rest=li[i]%42
    dic[str(rest)]=dic.get(str(rest),1)

print(len(list(dic.keys())))