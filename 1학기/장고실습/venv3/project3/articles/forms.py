from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField()

class ArticleModelForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        # 아티클모델에서 어느어느필드를 골라서 폼을 만들것인지 정해주는것.
        # 이렇게하면 모든 필드에대한 폼 다만듬


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField()

