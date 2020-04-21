from django.urls import path

from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('ask',views.ask,name='ask'),
    path(r'ds',views.ds,name='ds'),
    path(r'wd',views.wd,name='wd'),
    path(r'tags',views.tags,name='tags'),



        


]