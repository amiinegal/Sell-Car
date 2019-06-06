  
from .models import *
from django import forms

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['poster', 'usability', 'design', 'rating']


class RateForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['poster', 'average']



class RatingForm(forms.ModelForm):
    
    class Meta:
        model = CarEvaluate
        fields = ['design', 'usability']