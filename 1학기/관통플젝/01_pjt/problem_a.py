import json
from pprint import pprint
import os

path='./data/movies/'
file_list=os.listdir(path)   #해당 폴더의 파일이름들을 리스트로 반환함.

movies_list=[] # ./data/movies/ 하위의 파일들을 담을 빈 리스트를 생성.


# movies폴더안의 모든 파일을 하나의 리스트에 담는 코드.
for file_name in file_list:   
    with open(path+file_name, encoding='utf-8') as f:
        data = json.load(f)
    movies_list.append(data)


def movie_info(input):
    """
    영화의 정보를 담은 객체을 입력하면 해당 영화의 정보(json파일)가 출력되는 함수임.
    """
    result={'genre_ids':0,
        'id':0,
        'overview':0,
        'poster_path':0,
        'title':0,
        'vote_average':0    
    }

    result['genre_ids']=input['genre_ids']
    result['id']=input['id']
    result['overview']=input['overview']
    result['poster_path']=input['poster_path']
    result['title']=input['title']
    result['vote_average']=input['vote_average']

    return result

    # founded_movie=0
    # # 여기에 코드를 작성합니다.    
    # for i in movies_list:
    #     if i['title']==movie:
    #         founded_movie=i

    # pprint(i)
    # print('len',len(founded_movie['genres']))
    
    # # for i in range(len(founded_movie['genres'])):
    # #     result['genre_id'].append(founded_movie['genres'][i]['id'])
    # # result['id']=founded_movie['id']
    # # result['overview']=founded_movie['overview']
    # # result['title']=founded_movie['title']
    # # result['vote_average']=founded_movie['vote_average']
    # # pprint(result)
# movie_info(input)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))


