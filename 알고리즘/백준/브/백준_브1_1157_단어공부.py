str = input()
str=str.lower()

dic={}
for i in str:
    dic[i]=dic.get(i,0)+1

m=max(dic.values())

res=[]

for key,value in dic.items():
    if value==m:
        res.append(key)

if len(res)==1:
    print(''.join(res).upper())
else: 
    print('?')
