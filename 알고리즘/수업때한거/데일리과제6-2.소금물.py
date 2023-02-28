import re
from time import sleep

n=1
inputs=[]

for _ in range(5):
    dic={}
    inp=input(f'{n}. 소금물의 농도(%)와 소금물의 양(g)을 입력하시오: ')
    if inp=='Done':
        break
    dense_str, weight_str=inp.split()
    dense=int(re.sub(r'[^0-9]','',dense_str))
    weight=int(re.sub(r'[^0-9]','', weight_str))
    print('농도',dense,'양',weight)

    dic['번호']=dic.get('번호',n)
    dic['농도']=dic.get('농도',dense)
    dic['양']=dic.get('양', weight)
    
    inputs.append(dic)
    print(inputs)
    n+=1

sleep(1)
print('.......입력완료.......')
sleep(1.5)
print('입력된 소금물은 다음과 같습니다 :')
sleep(0.5)
print(inputs)
sleep(1.5)
print('소금물 섞는중...')

소금의양=0
물의양=0
for i in range (n-1):
    소금의양 += (inputs[i]['농도']/100)*inputs[i]['양']
    물의양 += inputs[i]['양']

전체농도 = (소금의양/물의양)*100
전체농도 = round(전체농도,2)

sleep(2)
print('소금물을 모두 섞었습니다!')
sleep(1)
print('농도 : ', 전체농도,'% , ','양 : ', 물의양,'g' )
