# 커스텀 필터를 만들것
# content 를 받아와 해시태그만 a 태그로 변경

# 필수 정의 영역
from django import template
from movies.models import Hashtag # from 앱.models import 모델
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe

register = template.Library()

# 내가 만든 커스텀 함수
# value: content 가 넘어옴
# arg: 뒤에 작성한 내용

# 등록 데코레이터
@register.filter
def set_hashtag(value):
    contents = value.replace('\r\n', ' ').split(' ')
    print('!', contents)
    for i in range(len(contents)):
        if contents[i].startswith('#'):
            hashtag = contents[i][1:]
            # #으로 시작하는 모든 단어는 무조건 해시태그다!!
            # 라는 확신이 없다면 버그남
            print('hhash',hashtag)
            try:
                hashtag_obj = Hashtag.objects.get(content=hashtag)
                # a 태그로 변경 
                contents[i] = f'<a href="{resolve_url("movies:hashtag", hashtag_obj.pk)}">#{hashtag}</a>'
            except Hashtag.DoesNotExist:
                pass

    return mark_safe(' '.join(contents))

    
# 커스텀 함수를 filter 에 등록
# register.filter('set_hashtag', set_hashtag)
