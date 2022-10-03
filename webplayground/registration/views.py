from audioop import reverse
from dataclasses import field
from pyexpat import model
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from matplotlib import widgets
from platformdirs import user_cache_dir
from .forms import UserCreationformWithEmail,Profileform,EmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

class signView(CreateView):
    form_class = UserCreationformWithEmail
    template_name= 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?register'

    #mejorando los stilos del formulario
    def get_form(self, form_class=None) :
        form=super(signView,self).get_form()
        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo@'})
        form.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar Contraseña'})
        
        form.fields['username'].label='' # ocultar los label
        form.fields['password1'].label=''
        form.fields['password2'].label=''
        return form   

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = Profileform
    
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'   

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile   
         
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        return self.request.user
# para que las validaciones sean en tiempo real
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar el email en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form
    
       
