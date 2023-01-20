import json
from pprint import pprint


def movie_info(input, gens):

    # 여기에 코드를 작성합니다.  
    
    result={
        'genre_names':0,
        'genre_ids':0,
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

    names=[]
    for id in result['genre_ids']:
        for gen in gens:
            if id==gen['id']:
                names.append(gen['name'])
    
    result['genre_names']=names
    
    del result['genre_ids']
    
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
