import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params ={
        "api_key" : '00f85b3ff3d0a50f7a66cc14f82143d6', # 문자열로 써준다.
        "language" : "ko",
        'region':'KR',
    
    }

    response = requests.get(BASE_URL + path, params = params).json()
    return len(response.get('results'))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
