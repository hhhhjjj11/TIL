import json
from pprint import pprint


def movie_info(movies, gens):
    
    # 여기에 코드를 작성합니다.  
    Ans=[]
    for input in movies:
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
        Ans.append(result)
        
    return Ans

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

