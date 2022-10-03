from dataclasses import fields
import profile
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from matplotlib import widgets
from .models import Profile

class UserCreationformWithEmail(UserCreationForm):
    email=forms.EmailField(required=True,help_text='Requerido debes ser minimo y valido')

    class Meta:
        model=User
        fields=("username","email","password1","password2")


#validacion para que solo se registre un solo correo
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u"El email ya está registrado, prueba con otro.")
        return email
class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['avatar','bio','link']
        widgets={
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio':forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3,'placeholder':'Biografia'}),
            'link':forms.URLInput(attrs={'class':'form-control mt-3','placeholder':'Link'}),
        }
        
class EmailForm(forms.ModelForm):
    email=forms.EmailField(required=True,help_text="Requerido es necesario ingrear los datos correspondientes")

    class Meta:
        model= User
        fields=['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email    


