from django import forms
from .models import Club, StudentMeta

class SearchForm(forms.Form):
    club = forms.ModelChoiceField(
        queryset = Club.objects, label='部活', required=False
    )

    student_meta = forms.ModelChoiceField(
        queryset = StudentMeta.objects, label='学年クラス', required=False
    )