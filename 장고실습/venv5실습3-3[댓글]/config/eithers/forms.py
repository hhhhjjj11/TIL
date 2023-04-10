from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'issue_a': "RED TEAM",
            'issue_b': "BLUE TEAM",
        }

class CommentForm(forms.ModelForm):
    # pick -> RED TEAM 선택시 0저장 , BLUE 선택시 1 저장
    pick = forms.ChoiceField(choices=[('0', 'RED TEAM'), ('1', 'BLUE TEAM')])
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('question',)

    