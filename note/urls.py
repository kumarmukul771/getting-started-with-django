from django.urls import path 
from .views import *


urlpatterns = [
    path('', homepage, name="home"),
    path('notes/', note, name='notes'),

    path('createnote/', createNote, name="note" ) #add this 
]