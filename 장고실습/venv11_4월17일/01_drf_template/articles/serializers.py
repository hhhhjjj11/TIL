from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):
    # 주의. 필드이름 마음대로 지으면 안됨. 역참조 매니저이름 써야됨. 안그러면 에러남.
    # 오른쪽 보세요. 어떤 모델 참조할건지 안썼죠? 필드이름을 역참조매니저로 간주하고 그로부터 모델을 참조하도록 만들어져있습니다.
    # 만약 필드이름 다르게 쓰고싶으면 모델에서 related_name으로 역참조매니저 이름 오버라이딩 해주면 됩니다.

    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    
    # 위와같이, PrimaryKeyRelatedField를 쓰면 조회시 각 comment들의 아이디만 나옵니다.
    # 다음과 같이 시리얼라이저를 다시 이용하면, 직렬화 시 연결된 데이터들 또한 함께 직렬화 하여 볼 수 있다.!! 필드이름과 같은 역참조매니저를 통해 역참조를 해서 직렬화할 때 함께 담아서 직렬화 하도록 함.
    # 즉, ArticleSerializer를 써서 article데이터를 직렬화 할 때, article데이터 외에 몇가지 항목을 더 불러와서(야 ~ 너도 와 ~ 같이 포장할거야 ~)(연결된 데이터) 함께 json으로 포장시켜준다 이 말임. HOW? -> 연결데이터의 시리얼라이저를 통해서.
    # 참고로, CommentSerializer가 윗줄에서 먼저 정의 되어 있어야 함. 아래줄에 있으면 안됨.
    comment_set = CommentSerializer(many=True, read_only=True)

    comment_count = serializers.IntegerField(source = 'comment_set.count', read_only = True)


    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = '__all__'
        # 필드추가시 메카클래스에서 필드는 반드시 all로 해주어야 함.
        # 필드 추가 또는 오버라이딩시 read_only_fields 가 동작하지 않으니 주의할 것 ! 그럼 어떡하냐? 위에 써놓은것처럼, 각 필드에서 read_only = True로 만들어줘야함.

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # rep은 key-value객체임

        # 키 이름 바꿔서 직렬화하기
        rep['comments'] = rep.pop('comment_set', []) # 두번째 인자는 만약에 'comment_set' key가 없을 경우 빈배열을 반환하도록 하는것.
        # 'comment_set' key 없애고 그 value를 'comments' key에 할당!
        # 이렇게 하면 직렬화할때 키 이름만 바꿀 수 있음. 
        
        # 특정 필드 빼고 직렬화하기
        rep.pop('article', None)
        
        return 