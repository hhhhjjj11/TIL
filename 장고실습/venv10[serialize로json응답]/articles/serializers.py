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
    
