
</br>
</br>

## [ 학습한 내용 ]
### 1. 특정사이트(TMDB)에서 제공하는 API 를 이용하는 방법에 대해 학습했다.
   - 홈페이지에서 API를 제공하는 버튼을 찾아서 누르면 관련 페이지를 볼 수 있다.
   - 이때 해당 페이지에 가입하여 API키(접근권한)을 얻어야한다.
   - 해당 페이지에서 제공하는 API관련 문서를 통해서 URL의 형태와 필요한 query parameter들을 확인한다.
   - 위에서 확인한 것들을 바탕으로 다음과 같이 코드를 작성하여 이용한다.
 - ```python
    import requests
     # BASE URL과 path를 따로 변수에 담아 이용하자.
     # 쿼리파라미터들도 따로 객체로 담아 아래처럼 적용한다.
    BASE_URL = 'https://api.themoviedb.org/3' 
    path = '/movie/popular'
    params ={
        "api_key" : '00f85b3ff3d0a50f7a66cc14f82143d6', # 문자열로 써준다.
        "language" : "ko",
        'region':'KR',
    }

    response = requests.get(BASE_URL + path, params = params).json()
    return len(response.get('results'))
    ```
- 구현하고자 하는 기능에 따라 해당 기관에서 제공하는 알맞은 API를 찾아서 이용한다.
- 이 PJT 에서는 다음의 API를 이용하였다.
  - 가장 인기 있는 영화 20개의 데이터를 얻을 수 있는 API
  - 제목을 입력받아 해당하는 영화의 데이터를 얻을 수 있는 API  
  - 키워드를 입력받아 추천영화 데이터를 얻을 수 있는 API
  - 영화의 id를 입력받아 출연진과 스태프등 크레딧 데이터를 얻을 수 있는 API

</br>
</br>

## [ 어려웠던 부분 ]
- API마다 쿼리와 path를 바꾸어주어야 한다는 것을 몰랐어서 잠시 헤맸다.

</br>
</br>

## [ 새로 배운 것들 및 느낀 점 ]
- 이전에 외부 API를 끌어다가 사용해본 경험은 없었어서 배워보고 싶었는데 이번 시간에 배울 수 있어서 좋았다.
- API마다 쿼리와 path를 바꾸어 주어야 한다는 것 또한 중요하게 기억해야할 것 같다.
- 코드를 작성하는 구체적 과정에서, Base_url과 path를 분리하여 변수에 담은 뒤 활용한다는 점
- 파라미터들 또한 객체로 만들어 한번에 적용한다는 점
- sorted 메소드를 이용하여 list를 재정렬할 때에 특정 키를 기준으로 하는 방법 (아래 코드)
  ```python
  
  # results 리스트를 각 항(movie)의 'vote_average'키를 기준으로 정렬, 내림차순으로 정렬. 0~4 까지.
  
  sorted(results, key=lambda movie: movie['vote_average'], reverse=True)[:5] 

  ```