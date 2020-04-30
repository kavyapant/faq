from django.urls import path

from .import views
urlpatterns = [
    path('',views.home,name='home'), 
    path(r'ds',views.ds,name='ds'),
    path(r'wd',views.wd,name='wd'),
    path(r'tags',views.tags,name='tags'),
    path('open',views.open,name='open'),
    path(r'answer',views.answer,name='answer'),
    path('camp_qs',views.camp_qs,name='camp_qs'), 
    path('ask_submit',views.ask_submit,name='ask_submit'),

    
    



        


]