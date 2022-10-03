from django.urls import path
from . import views
from .views import HomePageView,SamplePageView

urlpatterns = [
    #path('', views.home, name="home"),
    #path('sample/', views.sample, name="sample"),
    path('', HomePageView.as_view(), name='home'),
    path('sample/', HomePageView.as_view(), name='sample'),
]