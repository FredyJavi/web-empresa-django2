from pyexpat import model
from django import forms
from .models import Page

class Pageform(forms.ModelForm):

    class Meta:
        model= Page
        fields = ['title','content','order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden  '}),
        }
        labels = {
            'title':'', 'order':'', 'content': ''
        }
