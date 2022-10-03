from distutils.command.upload import upload
import profile
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) #relaciona con la tabla donde esta el usuario
    avatar=models.ImageField(upload_to='profiles',null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    link=models.URLField(max_length=200, null=True, blank=True)

#disparadores
@receiver(post_save,sender=User) # decorador se ejecuta despues de guardar
def ensure_profile_exists(sender,instance,**kwargs):
    if kwargs.get('created',False):
        profile.objects.get_or_create(user=instance)
        print("creacion de usuario")

