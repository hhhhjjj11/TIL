import math

N = int(input())   
li=[]



for _ in range(N):
    dict={}
    이름,학점,성적= input().split()
    dict['학점']=dict.get('학점',학점)
    dict['성적']=dict.get('성적',성적)
    li.append(dict)

score ={
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}


sum=0
total=0
for item in li:
    sum+=int(item['학점']) * score[item['성적']]
    total += int(item['학점'])

avg = sum/total
avg += 0.005
avg = (math.floor(100*avg))/100


print(f'{avg:.2f}')