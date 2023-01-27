import json
import os
from pprint import pprint

path='./data/movies/'
file_list=os.listdir(path)   #해당 폴더의 파일이름들을 리스트로 반환함.

movies_list=[] # ./data/movies/ 하위의 파일들을 담을 빈 리스트를 생성.


# movies폴더안의 모든 파일을 하나의 리스트에 담는 코드.
for file_name in file_list:   
    with open(path+file_name, encoding='utf-8') as f:
        data = json.load(f)
    movies_list.append(data)

#pprint(movies_list)
#for movie_ in movies_list:
#    print(movie_['revenue'])

revs=[]
for m2 in movies_list:
    dic={'title':m2['title'],
        'revenue':m2['revenue']
    }
    revs.append(dic)




def max_revenue(movies):
    # 여기에 코드를 작성합니다.  
    revlist=[]
    for movie in movies:
        for rev in revs:
            if movie['title']==rev['title']:
                #print(rev)
                revlist.append({'title': (rev['title']),'revenue' : (rev['revenue'])})

    Maxrev=0
    MaxName=0
    for i in revlist:
        if Maxrev<=i['revenue']:
            Maxrev=i['revenue']
            MaxName=i['title']
        # i[revenue]
        # 객체들을 가지고 있음. 이 안에서 값이 가장 큰놈을 찾아야함.
    return MaxName


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

