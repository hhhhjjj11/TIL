from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    # 주의. 필드이름 마음대로 지으면 안됨. 역참조 매니저이름 써야됨. 안그러면 에러남.
    # 오른쪽 보세요. 어떤 모델 참조할건지 안썼죠? 필드이름을 역참조매니저로 간주하고 그로부터 모델을 참조하도록 만들어져있습니다.
    # 만약 필드이름 다르게 쓰고싶으면 모델에서 related_name으로 역참조매니저 이름 오버라이딩 해주면 됩니다.
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    
    # 위와같이, PrimaryKeyRelatedField를 쓰면 조회시 각 comment들의 아이디만 나옵니다.
    # 내용을 원

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
