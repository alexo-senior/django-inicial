
# este archivo de urls.py se hace dentro de la app
#como buena practica para que la app este completa 

from django.contrib import admin
from django.urls import path
from . import views

#ya tenemos la ruta y esta siendo controlada por una vista en views


urlpatterns = [
    path('test/', views.test, name ='test'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name = 'delete'),
    
]


