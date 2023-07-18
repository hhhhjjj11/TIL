# 학습한내용
- CRUD, 모델폼 사용시 위젯적용, 프로젝트에서 스태틱 파일 사용하기

# 어려웠던 부분
- 위젯을 사용하는 부분과 스태틱을 사용하는 부분에서 막혔다.

# 새로 배운 것들 및 느낀점
- 위젯을 사용하는 부분과 스태틱을 사용하는 부분을 다시 배웠다.
- 위젯은 유튜브라이브때도 간단히 언급만하시고 넘어가서 거의 처음 해본느낌이었고,
- 스태틱파일 사용하는 부분은 분명 필기까지 다 해두었는데 공부를 꼼꼼히 하지 않아서 놓치고있었던 것 같다. 꼼꼼히 공부 해야겠다.

# 위젯
- 공식 문서 참고 : https://docs.djangoproject.com/ko/3.2/ref/settings/#std:setting-DATE_INPUT_FORMATS
- 구글링..
```python
from django import forms
from .models import Movie
from django.forms.widgets import DateInput, NumberInput


class MovieModelForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
                'score': NumberInput(
                attrs={'step':0.5,'min':0,'max':5,}
                ),
                'release_data': DateInput(attrs={'type':'date'})
            }

```
# 스태틱 파일
- settings.py에서
```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR/'static'
]
```
- 템플릿에서
```html
{% load static %}
{% block content %}
<img src="{% static 'movies/header.jpg' %}" alt="mainimage">
{% endblock%}
```
- 이미자파일 저장위치 : 앱 > static > 앱 > 이미지.jpg
