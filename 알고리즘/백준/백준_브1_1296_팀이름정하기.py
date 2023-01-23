name=input()   # JANE
N=int(input())  # 4
scrs=[]         
names=[]        

for i in range(N):
   
    dic={}

    dic['L']=dic.get('L',0)+name.count('L')
    dic['O']=dic.get('O',0)+name.count('O')
    dic['V']=dic.get('V',0)+name.count('V')
    dic['E']=dic.get('E',0)+name.count('E')

    cand=input()
    names.append(cand)

    dic['L']=dic.get('L')+cand.count('L')
    dic['O']=dic.get('O')+cand.count('O')
    dic['V']=dic.get('V')+cand.count('V')
    dic['E']=dic.get('E')+cand.count('E')
    
    L=dic['L']
    O=dic['O']
    V=dic['V']
    E=dic['E']

    score=((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    scrs.append(score)


# names=[THOMAS, MICHEAL, INDY, LIU]
# scores=[0,1,0,1]

Max=max(scrs)
Maxes=[]
for i in range(N):  
    if Max==scrs[i]:
        Maxes.append(names[i])

Maxes.sort()
# print(Maxes)
print(Maxes[0])