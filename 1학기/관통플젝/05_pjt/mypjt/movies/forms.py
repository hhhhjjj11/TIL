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
