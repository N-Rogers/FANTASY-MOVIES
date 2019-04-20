from movies.models import (
    moviecategory,
    movie
)
from django import forms
class categoryform(forms.ModelForm):

    class Meta:
        model = moviecategory
        fields = ('name',)
        

class movieform(forms.ModelForm):

    class Meta:
        model = movie
        fields=('category','movie_title','movie_file','istranslated',)