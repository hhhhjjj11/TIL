N = int(input())
fnames=[]
dic={}
for i in range(N):
    fname=list(input())[0]
    fnames.append(fname)

for i in range(N):
    dic[fnames[i]]=dic.get(fnames[i],0) + 1

res=[]
for key, value in dic.items():
    if value>=5:
        res.append(key)


if len(res)==0:
    print('PREDAJA')

res.sort()
print(''.join(res))