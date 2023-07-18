import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params ={
        "api_key" : '00f85b3ff3d0a50f7a66cc14f82143d6', # 문자열로 써준다.
        "language" : "ko",
        'query' : title,
        'region':'KR',
    }

    # 요청 및 응답

    try:
        response = requests.get(BASE_URL + path, params = params).json()
        results=response['results']
        results_exact_title=list(filter(lambda x: x['title']==title,results))
        id = results[0]['id']
        id = int(id)

        path = f'/movie/{id}/credits'
        params ={
            "api_key" : '00f85b3ff3d0a50f7a66cc14f82143d6', # 문자열로 써준다.
            "language" : "ko",
        }

        response2 = requests.get(BASE_URL + path, params = params).json()
        cast=response2['cast']
        crew=response2['crew']
        cast=list(filter(lambda x: x['cast_id']<10,cast))
        crew=list(filter(lambda x: x['department']=='Directing',crew))
        
        cast_name=[]

        for i in cast:
            cast_name.append(i['original_name'])

        crew_name=[]

        for i in crew:
            crew_name.append(i['original_name'])


        ans ={}
        ans['cast']=ans.get('cast', cast_name)
        ans['dicrecting']=ans.get('directing', crew_name)

        return ans

    except:
        return None



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
