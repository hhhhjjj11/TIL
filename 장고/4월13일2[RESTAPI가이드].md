
## REST API 디자인 가이드
  - REST API 설계의 가장 중요한 두 가지는 다음과 같다.

1. URI는 리소스를 표현해야 한다.(리소스명은 동사보다는 명사를 사용)
   - 행위에 대한 표현이 들어가지 말아야 한다.

2. 행위는 HTTP Method 로 표현한다.

```
GET /articles/1/delete/  -> X, url(자원)에 행위가 들어있음
DELETE /articles/1/      -> O, 자원에 대한 표현과 행위 구분
```
- 추가적인 몇가지 예시
```
# 전체 출력시
GET /articles/show/         -> X
GET /articles/              -> O

# 회원 추가 시
GET /articles/create/       -> X
POST /articles/             -> O
```

- REST API 설계 시 몇가지 규칙
1. 슬래시 구분자(/)는 계층 관계를 나타내는데 사용한다.
유저가 __가진__ devices 들 조회 : 'GET users/{userid}/devices'

2. 하이픈(-)은 URI 가독성을 높이는데 사용
3. 언더바(_)는 URI에 사용하지 않는다.

```
GET users/userexample/ -> X
GET users/userExample/ -> X
GET users/user_example/ -> X
GET users/user-example/ -> O
```

4. URI 에는 소문자를 사용해라
- RFC3986 (URI 문법 형식 표준) 대소문자를 구별하도록 규정
  - 대소문자에 따라 다른 리소스로 인식하기 때문에, 소문자로 쓰셈

5. 파일 확장자는 URI에 포함시키지 않는다.
  - Accept header 를 사용하여 확장자를 표현함
   
    ```
    GET articles/dog.jpg   -> X
    GET articels/dog HTTP/1.1   -> O
    ```
 - 수많은 규칙들이 존재해서 정확히 지키기가 너무 어렵다!
   - 많이 공부해야함

참고 : https://beyondj2ee.wordpress.com/2013/03/21/%EB%8B%B9%EC%8B%A0%EC%9D%98-api%EA%B0%80-restful-%ED%95%98%EC%A7%80-%EC%95%8A%EC%9D%80-5%EA%B0%80%EC%A7%80-%EC%A6%9D%EA%B1%B0/

https://www.youtube.com/watch?v=RP_f5dMoHFc

<br><br>

# serialize활용하는 방법
```python
from rest_framework import serializers
from .models import Article

# 시리얼라이즈 클래스를 정의하는 방법은 메타클래스를 이용하는 경우와 이용하지 않는경우가 있다.
# 메타클래스를 이용할경우 인자로 .ModelSerializer를 받으며 이 경우 모델에서 정의한 필드 중에서만 입출력이 가능하다.
# 메타클래스를 이용하지 않을경우 .Serializer를 입력 받으며 이 경우 사용자가 원하는 필드를 추가로 입력받거나 출력할 수 있게 된다. 이 경우 create매서드를 반드시 오버라이딩 해주어야 한다.


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

# Model이 붙으면 -> 정의한 필드에 대해서 입출력
# 안붙으면 -> 사용자가 원하는 필드를 추가로 입력 받거나, 출력함


# Serializer 사용
# 정의된 필드 외의 데이터를 사용자로부터 입력받고 싶을 때 사용
class ArticleSerializer(serializers.Serializer):

    content = serializers.CharField(max_length=100)
    title = serializers.CharField()
    created_at = serializers.CharField(read_only = True) # read_only를 지정하지 않으면 사용자가 입력을 해야함. 사용자의 입력을 받지 않고, 출력만 하길 원할 때.
    # required: 반드시 입력받아야하면 True
    # allow_blank : blank 허용
    # allow_null : null 값 허용
    myfield = serializers.CharField(write_only = True, required= False, allow_blank = True, allow_null = True)
    # write_only : 사용자의 입력만 받고, 출력은 하지 않길 원할 때

    # BaseSerializer 의 create() 함수가 호출됨
    # Serializers.Serializer 사용 시, create 를 반드시 재정의 해야함
    def create(self, validated_data):
        validated_data['title'] += validated_data['myfield']
        return Article.objects.create(
            title = validated_data['title'],
            content = validated_data['content'],
        )
        

    # update 메서드 오버라이딩
    # 아래처럼 작성하면 타이틀이랑 내용만 수정하는 것 인듯?
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
    
```