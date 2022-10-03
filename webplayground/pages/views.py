from ast import arg
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.admin.views.decorators import staff_member_required  #usando decoradores para la identificacion
from django.utils.decorators import method_decorator
from django.urls import reverse,reverse_lazy
from .models import Page
from .forms import Pageform
from django.shortcuts import redirect

#para herdar la funciones en otras
class StaffRequireMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs): ## permite comproboar si el usuario esta logeado en crear
        return super(StaffRequireMixin,self).dispatch(request,*args, **kwargs)


# Create your views here.
class PageListView(ListView):
    model=Page
    
class PageDetailView(DetailView):
    model=Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView): #creando vista con clases
    model = Page
    form_class=Pageform
    success_url=reverse_lazy('pages:pages')

  
class PageUpdate(StaffRequireMixin,UpdateView):
    model = Page
    form_class=Pageform
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

 
class PageDelete(StaffRequireMixin,DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    