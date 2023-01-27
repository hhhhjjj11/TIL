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


dates=[]
for movie in movies_list:
    dic={'title':movie['title'],
        'release_date':movie['release_date']
    }
    dates.append(dic)

#pprint(dates)


def dec_movies(movies):
    # 여기에 코드를 작성합니다.  
    datelist=[]
    for movie in movies:
        for date in dates:
            #print(date)
            if movie['title']==date['title']:
                #print(rev)
                datelist.append({'title': (date['title']),'release_date' : (date['release_date'])})

    Anslist=[]
    for item in datelist:
        if (int(list(item['release_date'])[5])==1) and (int(list(item['release_date'])[6])==2):
            Anslist.append(item['title'])

    return Anslist

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
